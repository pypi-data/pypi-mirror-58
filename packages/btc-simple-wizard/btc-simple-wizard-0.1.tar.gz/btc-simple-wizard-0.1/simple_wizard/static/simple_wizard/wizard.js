
djangoWizardAPI = {

    getAjaxMethod: function (method_name, url, data={}) {

        if (method_name.toLowerCase() === 'post') {
            return $.post(url, data)
        } else {
            return $.get(url)
        }
    },

    checkModalIsOpen: function (modal_object_or_selector) {
        return djangoWizardAPI.checkObjectSignature(modal_object_or_selector, 'in')
    },

    openModal: function (modal_object_or_selector) {
        const modal_object = djangoWizardAPI.getObject(modal_object_or_selector);
        const modal_is_open = djangoWizardAPI.checkModalIsOpen(modal_object_or_selector);

        if (!modal_is_open) {
            modal_object.modal('show');
        }
    },

    closeModal: function (modal_object_or_selector) {
        const modal_object = djangoWizardAPI.getObject(modal_object_or_selector);
        const modal_is_open = djangoWizardAPI.checkModalIsOpen(modal_object_or_selector);

        if (modal_is_open) {
            modal_object.modal('hide');
        }
    },

    loadInModal: function (step_to_load,
                           modal,
                           container,
                           management_url,
                           always_fetch=false,
                           method_name='get',
                           data={},
                           callback=null,
                           template_var='template',
                           hide_class='hidden') {

        const modal_object = djangoWizardAPI.getObject(modal);
        const container_object = djangoWizardAPI.getObject(container);
        const exist_containers_for_steps = djangoWizardAPI.getStepContainers(container_object);
        let container_for_step = djangoWizardAPI.getStepContainerByUniqueName(container_object, step_to_load);

        let need_fetch_from_server = true;
        if (!always_fetch && container_for_step.length) {
            need_fetch_from_server *= !container_for_step.data('cache-step');
        }

        if (need_fetch_from_server) {
            if (modal.length && container.length) {
                $.when(djangoWizardAPI.getAjaxMethod(method_name, management_url, data)).then(function (data) {
                    if (data[template_var]) {
                        if (data['reload_forward'] !== step_to_load) {
                            container_for_step =
                                djangoWizardAPI.getStepContainerByUniqueName(container_object, data['reload_forward']);
                            step_to_load = data['reload_forward'];
                        }
                        if (!container_for_step.length) {
                            container_for_step =
                                djangoWizardAPI.createStepContainerWrapper(container_object, step_to_load, data);
                        }
                        exist_containers_for_steps.addClass(hide_class);
                        container_for_step.html(data[template_var]);
                        container_for_step.removeClass(hide_class);
                        djangoWizardAPI.openModal(modal_object);

                        if (callback) {
                            callback(data);
                        }

                        $(document).trigger('django-wizard:step-loaded', step_to_load, method_name, data);
                    }
                })
            }
        } else {
            djangoWizardAPI.openModal(modal_object);
            exist_containers_for_steps.addClass(hide_class);
            container_for_step.removeClass(hide_class);
        }
    },

    createStepContainerWrapper: function (container, step_unique_name, data) {
        const container_object = djangoWizardAPI.getObject(container);
        const wrapper_object = djangoWizardAPI.getStepContainerWrapper();

        wrapper_object.attr('data-step-unique-name', step_unique_name);
        wrapper_object.attr('data-cache-step', data['cache_step'] || false);
        container_object.append(wrapper_object);

        return djangoWizardAPI.getStepContainerByUniqueName(container_object, step_unique_name);
    },

    getStepContainerByUniqueName: function (container, step_unique_name) {
        const container_object = djangoWizardAPI.getObject(container);
        return container_object.find(`.js-wizard_container[data-step-unique-name="${step_unique_name}"]`)
    },

    getStepContainers: function (container) {
        const container_object = djangoWizardAPI.getObject(container);
        return container_object.find('.js-wizard_container');
    },

    getStepContainerWrapper: function () {
        return $(`<div class="js-wizard_container"></div>`);
    },

    checkObjectSignature: function (target_object_or_selector, check_class=null, check_attrs=null) {
        const target_object = djangoWizardAPI.getObject(target_object_or_selector);
        let checks_passed = false;

        if (check_class != null) {
            checks_passed += target_object_or_selector.hasClass(check_class);
        }
        if (check_attrs != null) {
            $.each(check_attrs, function (key, value) {
                return  target_object.attr(key) === value;
            });
        }

        return checks_passed
    },

    getObject: function get_object(object_or_selector) {

        let result_object = undefined;

        typeof object_or_selector === 'object' ?
            result_object = object_or_selector :
            result_object = $(object_or_selector);

        return result_object
    }
};


DjangoModalWizard = function (modal_selector,
                              container_selector,
                              trigger_selector,
                              close_trigger_selector,
                              load_callback = null) {

    const self = this;

    this.modal_object = $(modal_selector);
    this.container_object = $(container_selector);
    this.trigger_selector = trigger_selector;
    this.close_trigger_selector = close_trigger_selector;

    this.loadInModal = function (trigger_object) {
        djangoWizardAPI.loadInModal(
            trigger_object.data('step-unique-name'),
            self.modal_object,
            self.container_object,
            trigger_object.data('management-url'),
            trigger_object.data('always-fetch'),
            'get',
            {},
            load_callback
        );
    };

    this.loadInModalByPost = function (trigger_object) {
        let post_data = self.container_object.find('input, select, textarea').serializeArray();
        post_data.push({name: trigger_object.attr('name'), value: trigger_object.attr('value')});
        djangoWizardAPI.loadInModal(
            trigger_object.data('step-unique-name'),
            self.modal_object,
            self.container_object,
            trigger_object.data('management-url'),
            trigger_object.data('always-fetch'),
            'post',
            post_data,
            load_callback
        );
    };

    this.initSignals = function () {
        $(document).on('click', self.trigger_selector, function (event) {
            const trigger_object = $(this);

            trigger_object.data('method') === 'post' ?
                self.loadInModalByPost(trigger_object) :
                self.loadInModal(trigger_object);

            event.preventDefault();
        });
        $(document).on('click', self.close_trigger_selector, function (event) {
            djangoWizardAPI.closeModal(self.modal_object);
            $(document).trigger('django-wizard:last-step-closed', self.modal_object);
            event.preventDefault();
        })
    };
};
