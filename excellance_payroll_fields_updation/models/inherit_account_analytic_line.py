from odoo import models,fields,api

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    overtime_amt = fields.Float('Overtime Amount')
    normal_hour = fields.Float('Normal Hour')
    weekend_or_holiday = fields.Boolean('Weekend/Holiday')
    month = fields.Selection([('01','January'),('02','February'),('03','March'),('04','April'),('05','May'),('06','June'),('07','July'),('08','August'),('09','September'),('10','October'),('11','November'),('12','December')],string='Month')
    updation_lines = fields.One2many('timesheet.updation.lines','timesheet_lines')

    # task_id = fields.Many2one('project.task', 'Task', compute='_compute_task_id', store=True, readonly=False, index=True,domain="[('company_id', '=', company_id), ('project_id.allow_timesheets', '=', True), ('project_id', '=?', project_id)]")
    # task_id = fields.Many2one('project.task', 'Task', store=True, readonly=False, index=True)

    # @api.depends('project_id')
    # def _compute_task_id(self):
    #     for line in self.filtered(lambda line: not line.project_id):
    #         line.task_id = False

    # @api.onchange('project_id', 'user_id')
    # def _domain_task_id(self):
    #     print("project_id",self.project_id.id)
    #     print("user_id",self.user_id.employee_id.id)
        # print("task_id",self.env['project.employees.main'].search([('project_ref','=',self.project_id.id),('employee_id','=',self.user_id.employee_id.id)]).mapped('task_id').name)
        # return {'domain': {'task_id':[('id', '=',self.env['project.employees.main'].search([('project_ref','=',self.project_id.id),('employee_id','=',self.user_id.employee_id.id)]).mapped('task_id'))]}}
        # return {'domain': {'task_id':[('employee_id', '=',self.employee_id.task_id)]}}
        # return {'domain': {'employee_id': [('job_id', '=', self.task_id.work_id.job_id.id),('state','=','no job')]}}

    @api.onchange('task_id')
    def onchange_normal_hour(self):
        if self.task_id:
            self.normal_hour = self.task_id.normal_hours

    @api.onchange('unit_amount')
    def onchange_overtime_amt(self):
        if self.unit_amount > self.normal_hour:
            overtime = self.unit_amount - self.normal_hour
            self.overtime_amt = overtime
        else:

            if self.unit_amount <= self.normal_hour:
                overtime = 0.00
                self.overtime_amt = overtime

    @api.onchange('date')
    def onchange_month_analytic_lines(self):
        print('mnbbmnbmb')
