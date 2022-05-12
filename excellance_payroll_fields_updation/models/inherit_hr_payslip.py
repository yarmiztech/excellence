from odoo import models,fields,api,_
from odoo.exceptions import UserError


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    income_amount = fields.Float('Other Income')
    other_deduction = fields.Float('Other Deduction')
    remarks = fields.Text('Remarks')
    currency_id = fields.Many2one("res.currency", readonly=True,related='company_id.currency_id')
    advance_payment = fields.Float('Advance Payment')



    def compute_sheet(self):
        super(HrPayslip, self).compute_sheet()
        total_days = 0
        total_basic_hours = 0
        overtime = 0
        overtime_lines = []
        if self.timesheet_lines:
            for days in self.timesheet_lines:
                if days.unit_amount > 0.00:
                    total_days += 1
            self.total_working_days = total_days
        else:
            self.total_working_days = total_days
        for hours in self.timesheet_lines:
            if hours.unit_amount != 0.00:
                total_basic_hours += hours.unit_amount - hours.overtime_amt
            else:
                total_basic_hours += hours.unit_amount
        self.total_basic_hours = total_basic_hours

        timesheets = self.env['account.analytic.line'].search([('employee_id', '=', self.employee_id.id)])
        total_amount = 0
        for time in timesheets:
            if time.date < self.date_from:
                timesheet = time.date.month
                from_date = self.date_from.month - 1
                if timesheet == from_date:
                    overtime += time.overtime_amt
                    self.total_overtime_previous_lines = None
                    lines =(0, 0,{
                        'date': time.date,
                        'previous_overtime_amount': time.overtime_amt
                    })
                    overtime_lines.append(lines)

        self.update({
            'total_overtime_previous_lines':overtime_lines
        })
        self.total_overtime_previous = overtime
        if self.struct_id.name == 'Monthly Salary Structure':
            timesheets = self.env['account.analytic.line'].search([('employee_id', '=', self.employee_id.id)])
            for time in timesheets:
                project_task = self.env['project.task'].search([('timesheet_ids', '=', time.ids)])
                for cost in project_task:

                    self.per_hour = cost.hour_charge
                    self.overtime_rate = cost.hour_charge
        else:
            if self.struct_id.name == 'Timesheet Salary Structure':
                self.timesheet_cost = self.employee_id.timesheet_cost
        # if self.struct_id.name == 'Monthly Salary Structure':
        #     for basic in self.line_ids.filtered(lambda a: a.code == 'BASIC'):
        #         basic.amount = self.total_working_days * self.daily_wage
        #         for ot in self.line_ids.filtered(lambda a: a.code == 'OT'):
        #             ot.amount = self.total_overtime_previous * self.overtime_rate
        #             print('bbjhbhj')

        if self.struct_id.name == 'Monthly Salary Structure':
            for basic in self.line_ids.filtered(lambda a: a.code == 'BASIC'):
                basic.amount = self.total_working_days * self.daily_wage
                for ovr in self.line_ids.filtered(lambda a: a.code == 'OT'):
                    ovr.amount = self.total_overtime_previous * self.overtime_rate
                    print('hhjh')
                    for net in self.line_ids.filtered(lambda a: a.code == 'NET'):
                        for ded in self.line_ids.filtered(lambda a: a.code == 'DED'):
                            for inc in self.line_ids.filtered(lambda a: a.code == 'INC'):
                                for gross in self.line_ids.filtered(lambda a: a.code == 'GROSS'):
                                    gross.amount = basic.amount + inc.amount + ovr.amount
                                    for lo in self.line_ids.filtered(lambda a: a.code == 'LO'):
                                        for adv in self.line_ids.filtered(lambda a: a.code == 'AD'):
                                            net.amount = basic.amount + ovr.amount + inc.amount - ded.amount + lo.amount - adv.amount




        else:
            for ovr in self.line_ids.filtered(lambda a: a.code == 'OT'):
                # print('ovr', ovr, ovr.amount)
                # prev_month = date.today().month - 1
                # # hr.employee
                # timesheets = self.env['account.analytic.line'].search([('employee_id', '=', self.employee_id.id)])
                # total_amount = 0
                # for time in timesheets:
                #     if time.date < self.date_from:
                #         timesheet = time.date.month
                #         from_date = self.date_from.month - 1
                #         if timesheet == from_date:
                #             overtime += time.overtime_amt

                # for amt in project_task:
                # total_amount += overtime * self.employee_id.timesheet_cost
                # ovr.amount = total_amount
                ovr.amount = self.total_overtime_previous * self.timesheet_cost
                for time in self.line_ids.filtered(lambda a: a.code == 'TS'):
                    for ded in self.line_ids.filtered(lambda a: a.code == 'DED'):
                        for inc in self.line_ids.filtered(lambda a: a.code == 'INC'):
                            for lo in self.line_ids.filtered(lambda a: a.code == 'LO'):
                                for ovr in self.line_ids.filtered(lambda a: a.code == 'OT'):
                                    for gross in self.line_ids.filtered(lambda a: a.code == 'GROSS'):
                                        gross.amount = time.amount + inc.amount + ovr.amount

                                        for adv in self.line_ids.filtered(lambda a: a.code == 'AD'):
                                            for net in self.line_ids.filtered(lambda a: a.code == 'NET'):
                                                net.amount = time.amount + ovr.amount + inc.amount - ded.amount + lo.amount - adv.amount


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    timesheet_cost = fields.Monetary('Hourly Rate', currency_field='currency_id',groups="hr.group_hr_user", default=0.0)
