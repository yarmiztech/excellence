from odoo import models,fields,api,_
from odoo.exceptions import UserError


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    employee = fields.Boolean('Employee',compute='default_employee_access')


    def default_employee_access(self):
        if self.env.user.user_has_groups('enz_manpower_access.employee_access_group') == True:
            self.employee = True
        else:
            self.employee = False


    def compute_sheet(self):
        if self.employee == True:
            raise UserError(_('Only Manager has the acces for Sheet Computation'))
        super(HrPayslip, self).compute_sheet()


