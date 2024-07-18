odoo.define('cloud_cti.call_button', function (require) {
    "use strict";
    var core = require('web.core');
    var Widget = require('web.Widget');
    var rpc = require('web.rpc');
    var FormController = require('web.FormController');

    FormController.include({
        _onCallButtonClick: function () {
            var self = this;
            var phoneNumber = this.record.data.phone_number;

            rpc.query({
                model: 'cloud.cti',
                method: 'initiate_call',
                args: [phoneNumber]
            }).then(function (result) {
                if (result) {
                    var iframe = document.getElementById('cti_iframe');
                    if (iframe) {
                        iframe.contentWindow.postMessage({ phone_number: phoneNumber }, '*');
                    }
                }
            });
        },
        renderButtons: function ($node) {
            this._super($node);
            if (this.$buttons) {
                var $callButton = this.$buttons.find('.o_form_button_call');
                if ($callButton.length) {
                    $callButton.click(this._onCallButtonClick.bind(this));
                }
            }
        }
    });

    return Widget;
});

