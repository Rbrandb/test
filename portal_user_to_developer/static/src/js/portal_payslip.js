
odoo.define('portal_user_to_developer.portal_payslip',function(require){
    'use strict';
    var publicWidget = require('web.public.widget');
    var rpc = require('web.rpc');
    var session = require('web.session');
    publicWidget.registry.portal_payslip = publicWidget.Widget.extend({
        selector: ".payslip",
//        template: 'portal_time_off_details',
//         events: {
//                'click #button-40':'onclick_time_off_type',
//        },


        willStart: function(){
        var self = this;
        console.log('willStartwillStartwillStart111111111111')
        return this._super()
        .then(function() {
            var def0 = []
//            const description = document.getElementById('description');
//            const myfile = document.getElementById('myfile');
//            const date_from = document.getElementById('date_from');
//            const date_to = document.getElementById('date_to');
//            description.value = '';
//            myfile.value = '';
//            date_from.value = '';
//            date_to.value = '';
            $("#datepicker").datepicker( {
            format: "mm-yyyy",
            startView: "months",
            minViewMode: "months"
            });
        return $.when(def0);
        });
        },
//
//        onclick_time_off_type :function(events){
////        var user = session.uid
////        var option = $(events.target).val();
//        console.log('oooooooooo');
////        const firstNameInput = document.getElementById('description');
////        firstNameInput.value = '';
//
//
////        var self = this
////            rpc.query({
////                model: "time.off.type",
////                method: "get_time_of_types",
////            }).then(function (result) {
////                console.log('result', result)
////                for (var c in result) {
////                    console.log('resultc', result[c].name)
////                    $('#time_off_type').append('<option value="' + result[c].id + '">' + result[c].name + '</option>')
////               };
////            });
//        },
    });

});

