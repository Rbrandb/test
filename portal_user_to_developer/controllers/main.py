# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import binascii
import base64
from werkzeug.utils import redirect
import io
from odoo import fields, http, SUPERUSER_ID, _
from odoo.exceptions import AccessError, MissingError, ValidationError
from odoo.fields import Command
from odoo.http import request
from datetime import timedelta
from datetime import datetime, timedelta
from odoo.addons.portal.controllers import portal


class CustomerPortal(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        if 'time_off_count' in counters:
            values['time_off_count'] = None

        payslip = request.env['hr.payslip'].sudo().search([])
        employee = request.env['employee.hub'].sudo().search([
            ('portal_user_id', '=', request.uid)])
        if 'payslip_count' in counters:
            values['payslip_count'] = None
        return values




class DeveloperPortal(http.Controller):

    @http.route(['/my/avware_unit', '/my/avware_unit/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_orders(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):

        return request.render("portal_user_to_developer.portal_time_off_details")

    @http.route(['/my/payslip', '/my/payslip/page/<int:page>'], type='http', auth="user", website=True)
    def portal_pay_slips(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):

        return request.render("portal_user_to_developer.my_payslip_template", )

    @http.route('/payslip/submits', website=True, auth='user', csrf=False)
    def submit_payslip(self, **kwargs):
        d1 = datetime.strptime(str(kwargs.get('start date')), '%Y-%m')
        empolyee = request.env['employee.hub'].sudo().search([
            ('portal_user_id', '=', request.uid)])
        employee = empolyee.employee_id.id
        document = request.env['documents.document'].sudo().search([('employee_id', '=', employee), ('payslip_date', '!=', False)])
        docu = document.filtered(lambda x: int(fields.Date.from_string(x.payslip_date).strftime('%m')) == int(d1.month) and int(fields.Date.from_string(x.payslip_date).strftime('%Y')) == int(d1.year))
        document_id = docu.attachment_id
        time_ff = request.env['portal.time.off'].sudo().search([
            ('attachment', '!=', False)])

        document_url = time_ff.attachment
        return request.render("portal_user_to_developer.my_payslip_template", {'document': document_id})

    @http.route(['/to_submit', '/to_submit/page/<int:page>'], type='http', auth="user", website=True)
    def portal_to_submit(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        empolyee = request.env['employee.hub'].sudo().search([
            ('portal_user_id', '=', request.uid)])
        employee = empolyee.employee_id.id
        my_time_offs = request.env['portal.time.off'].sudo().search([
            ('employee_id', '=', employee), ('state', '=', 'draft')])
        value = []
        for my_time_off in my_time_offs:
            value.append({
                'type': my_time_off.time_off_type.name,
                'from': my_time_off.request_date_from,
                'to': my_time_off.request_date_to,
                'description': my_time_off.name
            })
        values = {
            'value': value
        }
        return request.render("portal_user_to_developer.my_time_off_details", values)

    @http.route(['/to_approve', '/to_approve/page/<int:page>'], type='http', auth="user", website=True)
    def portal_to_approve(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        empolyee = request.env['employee.hub'].sudo().search([
            ('portal_user_id', '=', request.uid)])
        employee = empolyee.employee_id.id
        my_time_offs = request.env['portal.time.off'].sudo().search([
            ('employee_id', '=', employee), ('state', '=', 'confirm')])
        value = []
        for my_time_off in my_time_offs:
            value.append({
                'type': my_time_off.time_off_type.name,
                'from': my_time_off.request_date_from,
                'to': my_time_off.request_date_to,
                'description': my_time_off.name
            })
        values = {
            'value': value
        }
        return request.render("portal_user_to_developer.my_time_off_details", values)

    @http.route(['/refused', '/to_submit/page/<int:page>'], type='http', auth="user", website=True)
    def portal_refused(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        empolyee = request.env['employee.hub'].sudo().search([
            ('portal_user_id', '=', request.uid)])
        employee = empolyee.employee_id.id
        my_time_offs = request.env['portal.time.off'].sudo().search([
            ('employee_id', '=', employee), ('state', '=', 'refuse')])
        value = []
        for my_time_off in my_time_offs:
            value.append({
                'type': my_time_off.time_off_type.name,
                'from': my_time_off.request_date_from,
                'to': my_time_off.request_date_to,
                'description': my_time_off.name
            })
        values = {
            'value': value
        }
        return request.render("portal_user_to_developer.my_time_off_details", values)

    @http.route(['/second_approval', '/second_approval/page/<int:page>'], type='http', auth="user", website=True)
    def portal_second_approval(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        empolyee = request.env['employee.hub'].sudo().search([
            ('portal_user_id', '=', request.uid)])
        employee = empolyee.employee_id.id
        my_time_offs = request.env['portal.time.off'].sudo().search([
            ('employee_id', '=', employee), ('state', '=', 'validate1')])
        value = []
        for my_time_off in my_time_offs:
            value.append({
                'type': my_time_off.time_off_type.name,
                'from': my_time_off.request_date_from,
                'to': my_time_off.request_date_to,
                'description': my_time_off.name
            })
        values = {
            'value': value
        }
        return request.render("portal_user_to_developer.my_time_off_details", values)

    @http.route(['/approved', '/approved/page/<int:page>'], type='http', auth="user", website=True)
    def portal_approved(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        empolyee = request.env['employee.hub'].sudo().search([
            ('portal_user_id', '=', request.uid)])
        employee = empolyee.employee_id.id
        my_time_offs = request.env['portal.time.off'].sudo().search([
            ('employee_id', '=', employee), ('state', '=', 'validate')])
        value = []
        for my_time_off in my_time_offs:
            value.append({
                'type': my_time_off.time_off_type.name,
                'from': my_time_off.request_date_from,
                'to': my_time_off.request_date_to,
                'description': my_time_off.name
            })
        values = {
            'value': value
        }
        return request.render("portal_user_to_developer.my_time_off_details", values)

    @http.route('/timeoff/submits', website=True, auth='user', csrf=False)
    def submit_magento(self, **kwargs):
        empolyee = request.env['employee.hub'].sudo().search([
            ('portal_user_id', '=', request.uid)])
        # print(empolyee)
        user_id = request.env['res.users'].sudo().search([
            ('employee_responsible', '=', True)])
        if not empolyee:
            raise ValidationError(_('Employee not linked to user'))
        d1 = datetime.strptime(kwargs.get('start date'), '%Y-%m-%d')
        d2 = datetime.strptime(kwargs.get('to date'), '%Y-%m-%d')
        d3 = d2 - d1
        total_days = str(d3.days)
        time_off = request.env['portal.time.off'].create({
            'name': kwargs.get('description'),
            'user_id': user_id.id,
            'employee_id': empolyee.employee_id.id,
            'time_off_type': int(kwargs.get('time_off_type')),
            'request_date_from': kwargs.get('start date'),
            'request_date_to': kwargs.get('to date'),
            'number_of_days': int(total_days),
            # 'company_id': 1
        })

        Attachments = request.env['ir.attachment']
        # post.get('attachment').filename/
        name = kwargs.get('myfile').filename
        file = kwargs.get('myfile')

        attachment_id = Attachments.sudo().create({

            'name': name,

            'type': 'binary',

            'datas': base64.b64encode(file.read()),

            'res_model': 'portal.time.off',

            'res_id': time_off.id

        })

        time_off.update({

            'attachment': [(4, attachment_id.id)],

        })

        return request.render("portal_user_to_developer.time_off_done")

    @http.route(['/attachment/download', ], type='http', auth='public')
    def download_attachment(self, attachment_id):
        # Check if this is a valid attachment id
        attachment = request.env['ir.attachment'].sudo().search(
            [('id', '=', int(attachment_id))])

        if attachment:
            attachment = attachment[0]
        else:
            return redirect('/shop')

        if attachment["type"] == "url":
            if attachment["url"]:
                return redirect(attachment["url"])
            else:
                return request.not_found()
        elif attachment["datas"]:
            data = io.BytesIO(base64.standard_b64decode(attachment["datas"]))
            return http.send_file(data, filename=attachment['name'],
                                  as_attachment=True)
        else:
            return request.not_found()

