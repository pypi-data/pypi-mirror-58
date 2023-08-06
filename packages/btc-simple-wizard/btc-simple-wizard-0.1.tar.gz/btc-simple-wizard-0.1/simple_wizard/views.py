import inspect
from typing import Callable, Type, Union

from django.http import JsonResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View


class ButtonsMixin:
    """
    Mixin for adding buttons to the view context
    """

    buttons: list = []
    parent_view: Type[View]() = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_buttons_management_url()

    def set_buttons_management_url(self) -> None:
        management_url_pattern = getattr(self.parent_view, 'management_url_pattern', None)
        if management_url_pattern is not None:
            for button in self.get_buttons():
                if hasattr(button, 'management_url'):
                    if not button.management_url:
                        button.management_url = reverse_lazy(
                            management_url_pattern, kwargs=self.get_url_kwargs(button=button)
                        )

    def get_url_kwargs(self, **kwargs) -> dict:
        button = kwargs['button']
        url_kwargs = getattr(self.parent_view, 'kwargs', {})
        url_kwargs.update({'step_to_load': button.load_step})
        return url_kwargs

    def get_buttons(self) -> list:
        return self.buttons

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(dict(
            buttons=self.get_buttons()
        ))
        return context


class JsonContextMixin:
    """
    An extra context mixin that passes the keyword arguments received by
    get_json_response_data() as the JsonResponse context.
    """

    json_extra_context: dict = None

    def get_json_response_data(self, **kwargs) -> dict:
        if self.json_extra_context is not None:
            kwargs.update(self.json_extra_context)
        return kwargs


class WizardStepMixin(JsonContextMixin):
    """
    A step view mixin for steps
    """

    unique_name: str = None
    cache_step: bool = True  # cancel to fetch step from server on reload
    reload_forward: str = None

    parent_view: Type[View]() = None

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return self.get_json_response(response)

    def get_json_response(self, http_response: Type[HttpResponse]()) -> JsonResponse:
        data = self.get_json_response_data(template=http_response.rendered_content)
        return JsonResponse(data, safe=False)

    def get_json_response_data(self, **kwargs) -> dict:
        json_response_data = super().get_json_response_data(**kwargs)
        json_response_data.update({
            'cache_step': self.cache_step,
            'reload_forward': self.reload_forward or self.unique_name,
        })
        return json_response_data

    def redirect_to_step(self,
                         step_unique_name: str,
                         management_url_pattern: str = None) -> Union[
        HttpResponseRedirect, HttpResponsePermanentRedirect]:
        self.reload_forward = step_unique_name
        url_pattern = management_url_pattern or getattr(self.parent_view, 'management_url_pattern', None)
        url_kwargs = getattr(self.parent_view, 'kwargs', {})
        url_kwargs.update({'step_to_load': step_unique_name})
        return redirect(url_pattern, *url_kwargs.values())


class WizardStepTitleMixin:
    """
    A step mixin for add title
    """

    title: str = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title
        })
        return context


class WizardStepMessageMixin:
    """
    A step mixin for add message
    """

    message: str = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'message': self.message
        })
        return context


class WizardModalStepMixin(ButtonsMixin, WizardStepTitleMixin, WizardStepMixin):
    """
    A base mixin for modal views
    """

    pass


class WizardModalStepWithMessageMixin(WizardStepMessageMixin, WizardModalStepMixin):
    """
    Mixin for message-modal-views
    """

    pass


class WizardModalStepWithFormMixin(WizardModalStepMixin):
    """
    Mixin for modal views with forms (FormView / CreateView /UpdateView)
    """

    redirect_to_step_if_valid: str = ''

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return self.get_json_response(response)

    def form_valid(self, form):
        return self.redirect_to_step(self.redirect_to_step_if_valid)


class WizardMixin:
    """
    Mixin for wizard implementation
    """

    _view_lookup_name: str = 'step_to_load'
    _check_methods: list = ['GET', 'POST']

    management_url: str = None
    common_title: str = ''

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.check_members()

    def check_members(self) -> None:
        # check member views unique names
        class_members = [
            member for _, member in inspect.getmembers(self)
            if inspect.isclass(member) and issubclass(member, WizardStepMixin)
        ]
        for member in class_members:
            member_unique_name = member.unique_name
            if not member_unique_name:
                raise RuntimeError('Не установлен параметр "unique_name" для представления %s' % member.__name__)
            if not hasattr(self, member_unique_name):
                setattr(self, member_unique_name, member)
            else:
                raise RuntimeError(
                    'Атрибут "unique_name" : "%s" дочерних элементов должен быть уникальным в '
                    'пределах %s' % (member_unique_name, self.__class__.__name__)
                )

            # setting model class to child views
            model = getattr(self, 'model', None)
            if model:
                setattr(member, 'model', model)

            # setting common title to all members that has no one
            if hasattr(member, 'title') and not getattr(member, 'title', None):
                setattr(member, 'title', self.common_title)

    def dispatch(self, request, *args, **kwargs):
        step_view_response = self.get_step_view_router()
        if step_view_response:
            response = step_view_response(request, *args, **kwargs)
        else:
            raise RuntimeError('Не удалось найти представление-обработчик для переданного "_view_lookup_name"')
        return response

    def get_step_view_name_form_query_data(self) -> str:
        # get view name from view-method "QueryDict" data
        step_view_name = None
        for method in self._check_methods:
            query_dict = getattr(self.request, method, None)
            if query_dict:
                step_view_name = query_dict.get(self._view_lookup_name)
                if step_view_name:
                    break

        return step_view_name

    def get_step_view_name_from_url(self) -> str:
        return self.kwargs.get(self._view_lookup_name)

    def get_step_view_router(self, name: str = None) -> Callable:
        # get view name from view-method "QueryDict" data or from url
        step_view_name = name or self.get_step_view_name_from_url() or self.get_step_view_name_form_query_data()
        # get view response
        step_view_response = None
        if step_view_name:
            target_view_class = getattr(self, step_view_name, None)
            if target_view_class:
                setattr(target_view_class, 'parent_view', self)
                step_view_response = target_view_class.as_view()
        return step_view_response
