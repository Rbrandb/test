# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ResUserInherit(models.Model):
    _inherit = 'res.users'

    employee_responsible = fields.Boolean(
        'Employee responsible',
        domain="[('sel_groups_1_9_10', '=', '1')]",
        )

    @api.onchange('employee_responsible')
    def _onchange_employee_responsible(self):
        employee_responsible = self.env['res.users'].search([('employee_responsible', '=', True)])
        print('employee_responsible', employee_responsible)
        employee_ = self.env['res.users'].search([])
        for rec in employee_:
            print(rec.name, rec.partner_share)
        if employee_responsible:
            print(employee_responsible.partner_share)
            raise ValidationError(_('Already a user have assigned employee responsible'))



