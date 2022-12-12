# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class HrLeaveType(models.Model):
    _inherit = 'hr.leave.type'

    @api.model
    def create(self, vals):
        print("HrLeaveType", vals)
        res = super(HrLeaveType, self).create(vals)
        print(vals.get('name'))
        self.env['time.off.type'].create({
            'name': vals.get('name'),
            'time_off_id': res.id
        })
        return res

    # @api.depends('state')
    # def change_state(self):
    #     print('dataaaaaaaaaaaaaa')
