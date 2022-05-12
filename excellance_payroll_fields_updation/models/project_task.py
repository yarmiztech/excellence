from odoo import models,fields,api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    employee_id = fields.Many2one('hr.employee','Employee')
    # employee_id = fields.Many2one('hr.employee','Employee',compute='compute_employee_ids')
    timesheet_lines = fields.Integer('Timesheet lines',compute = '_compute_timesheet_ids_lines')
    updation_lines = fields.One2many('timesheet.updation.lines','timesheet_lines')



    def _compute_timesheet_ids_lines(self):
        count = 0
        for i in self.timesheet_ids:
            count +=1
            self.timesheet_lines = count
        return self.timesheet_lines


    # def compute_employee_ids(self):
    #     for emp in self.employee_ids:
    #         if emp.employee_id:
    #             self.employee_id = emp.employee_id.id


    # def onchange_updation_lines(self):
    #     month = 0
    #     total_lines = []
    #
    #     for time in self.timesheet_ids:
    #         month = time.date.month
    #     if month == 1:
    #         months = None
    #         # total_lines = []
    #         total_hours = 0.00
    #         days =0
    #         employee_id = None
    #         task_id = None
    #         self.updation_lines = None
    #         for timesheet in self.timesheet_ids.filtered(lambda a:a.date.month == 1):
    #             days += 1
    #             employee_id = timesheet.employee_id.id
    #             months = '01'
    #             if timesheet.unit_amount > 0.00:
    #                 total_hours += timesheet.unit_amount
    #             else:
    #                 total_hours += timesheet.overtime_amt
    #         lines = (0, 0, {
    #             'month': months,
    #             'employee_id': employee_id,
    #             'task_id': self.name,
    #             'days': days,
    #             'total_hours_per_month': total_hours
    #
    #         })
    #         total_lines.append(lines)
    #     # self.update({
    #     #     'updation_lines': total_lines
    #     # })
    #     if month == 6:
    #         months = None
    #         # total_lines = []
    #         total_hours = 0.00
    #         days =0
    #         employee_id = None
    #         task_id = None
    #         self.updation_lines = None
    #         for timesheet in self.timesheet_ids.filtered(lambda a:a.date.month == 6):
    #             days += 1
    #             employee_id = timesheet.employee_id.id
    #             months = '06'
    #             if timesheet.unit_amount > 0.00:
    #                 total_hours += timesheet.unit_amount
    #             else:
    #                 total_hours += timesheet.overtime_amt
    #         lines = (0, 0, {
    #             'month': months,
    #             'employee_id': employee_id,
    #             'task_id': self.name,
    #             'days': days,
    #             'total_hours_per_month': total_hours
    #
    #         })
    #         total_lines.append(lines)
    #     self.update({
    #         'updation_lines': total_lines
    #     })



    # @api.model
    # def create(self, vals):
    #     total_list = []
    #
    #     for timesheet in self.timesheet_ids:
    #         total_list = []
    #         month = None
    #
    #         self.updation_lines = None
    #         if timesheet.date:
    #             month = timesheet.date.month
    #             print('timesheet.date', month)
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 1):
    #             month = "01"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             print("task_id", task_id)
    #
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #         line = (0, 0, {
    #             'month': month,
    #             'employee_id': employee_id,
    #             'task_id': task_id,
    #             'days': days,
    #             'total_hours_per_month': total_hours,
    #
    #         })
    #         print("line", line)
    #         total_list.append(line)
    #         # self.update({
    #         #     'updation_lines': total_list
    #         # })
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 5):
    #             month = "05"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             print("task_id", task_id)
    #
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #         line = (0, 0, {
    #             'month': month,
    #             'employee_id': employee_id,
    #             'task_id': task_id,
    #             'days': days,
    #             'total_hours_per_month': total_hours,
    #
    #         })
    #         print("line", line)
    #
    #         total_list.append(line)
    #     self.update({
    #         'updation_lines': total_list
    #     })
    #     res = super(ProjectTask, self).create()
    #
    #     return res




    # def onchange_updation_lines(self):
    #     total_lines = []
    #     days = 0
    #     total_hours = 0.00
    #     self.updation_lines = None
    #     month = None
    #     employee_id = None
    #     task_id = None
    #     for timesheet in self.timesheet_ids:
    #         total_lines = []
    #         days = 0
    #         total_hours = 0.00
    #         self.updation_lines = None
    #         month = timesheet.date.month
    #         employee_id = timesheet.mapped('employee_id').id
    #         task_id = self.name
    #         if month == 1:
    #             months = '01'
    #             total_lines = []
    #             days = 0
    #             total_hours = 0.00
    #             for timesheet in self.timesheet_ids.filtered(lambda a: a.date.month == 1):
    #                 days += 1
    #                 if timesheet.unit_amount > 0.00:
    #                     total_hours += timesheet.unit_amount
    #                 else:
    #                     total_hours += timesheet.overtime_amt
    #             lines = (0, 0, {
    #                 'month': months,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours
    #             })
    #             total_lines.append(lines)
    #
    #     self.update({
    #         'updation_lines': total_lines
    #     })
    #
    #     if month == 5:
    #         months = '05'
    #         total_lines = []
    #         days = 0
    #         total_hours = 0.00
    #         for timesheet in self.timesheet_ids.filtered(lambda a: a.date.month == 5):
    #             days += 1
    #             if timesheet.unit_amount > 0.00:
    #                 total_hours += timesheet.unit_amount
    #                 # total_hours = sum(self.timesheet_ids.filtered(lambda a:a.date.month==5).mapped('unit_amount'))
    #             else:
    #                 total_hours += timesheet.overtime_amt
    #                 # total_hours = sum(self.timesheet_ids.filtered(lambda a:a.date.month==5).mapped('overtime_amt'))
    #         lines = (0, 0, {
    #             'month': months,
    #             'employee_id': employee_id,
    #             'task_id': task_id,
    #             'days': days,
    #             'total_hours_per_month': total_hours
    #         })
    #         total_lines.append(lines)
    #
    #
    #     self.update({
    #         'updation_lines': total_lines
    #     })
    #     # self.updation_lines = None


    # def onchange_updation_lines(self):
    #     if self.timesheet_ids:
    #         days = 0
    #         total_hours = 0.00
    #         month = 0
    #         employee_id = None
    #         task_id = None
    #         self.updation_lines = None
    #
    #         for timesheet in self.timesheet_ids:
    #             month = timesheet.date.month
    #         if month == 1:
    #             months = '01'
    #             total_lines = []
    #             # for timesheet in self.timesheet_ids.filtered(lambda a: a.date.month == 1):
    #             for timesheet in self.timesheet_ids:
    #                 if month == 1:
    #
    #                     employee_id = timesheet.mapped('employee_id').id
    #                     task_id = self.name
    #                     days += 1
    #                     if timesheet.unit_amount > 0.00:
    #                         total_hours += timesheet.unit_amount
    #                     else:
    #                         total_hours += timesheet.overtime_amt
    #                 lines = (0, 0, {
    #                     'month': months,
    #                     'employee_id': employee_id,
    #                     'task_id': task_id,
    #                     'days': days,
    #                     'total_hours_per_month': total_hours
    #                 })
    #                 total_lines.append(lines)
    #
    #         if month == 2:
    #             months = '02'
    #             total_lines = []
    #             for timesheet in self.timesheet_ids.filtered(lambda a: a.date.month == 2):
    #                 employee_id = timesheet.mapped('employee_id').id
    #                 task_id = self.name
    #                 days += 1
    #                 if timesheet.unit_amount > 0.00:
    #                     total_hours += timesheet.unit_amount
    #                 else:
    #                     total_hours += timesheet.overtime_amt
    #             lines = (0, 0, {
    #                 'month': months,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours
    #             })
    #             total_lines.append(lines)
    #
    #         if month == 5:
    #             months = '05'
    #             total_lines = []
    #             for timesheet in self.timesheet_ids.filtered(lambda a: a.date.month == 5):
    #                 employee_id = timesheet.mapped('employee_id').id
    #                 task_id = self.name
    #                 days += 1
    #                 if timesheet.unit_amount > 0.00:
    #                     total_hours += timesheet.unit_amount
    #                 else:
    #                     total_hours += timesheet.overtime_amt
    #             lines = (0, 0, {
    #                 'month': months,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours
    #             })
    #             total_lines.append(lines)
    #
    #         if month == 6:
    #             months = '06'
    #             total_lines = []
    #             for timesheet in self.timesheet_ids.filtered(lambda a: a.date.month == 6):
    #                 employee_id = timesheet.mapped('employee_id').id
    #                 task_id = self.name
    #                 days += 1
    #                 if timesheet.unit_amount > 0.00:
    #                     total_hours += timesheet.unit_amount
    #                 else:
    #                     total_hours += timesheet.overtime_amt
    #             lines = (0, 0, {
    #                 'month': months,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours
    #             })
    #             total_lines.append(lines)
    #         self.update({
    #             'updation_lines': total_lines
    #         })

    def onchange_updation_lines(self):
        month = None
        self.updation_lines = None

        for time in self.timesheet_ids:
            month = time.date.month
        days = 0
        total_hours = 0.00
        employee_id = None
        task_id = None
        months = None
        total_lines = []
        # self.updation_lines = None
        for timsheet in self.timesheet_ids.filtered(lambda a: a.date.month == 1):
            # if month == 1:
            months = '01'
            employee_id = timsheet.employee_id.id
            task_id = self.name
            days += 1
            if timsheet.unit_amount > 0.00:
                total_hours += timsheet.unit_amount
            else:
                total_hours += timsheet.overtime_amt
        lines = (0, 0, {
            'month': months,
            'employee_id': employee_id,
            'task_id': task_id,
            'days': days,
            'total_hours_per_month': total_hours,
        })
        print("lines",lines)
        if total_hours != 0.00:

            total_lines.append(lines)
        self.update({
            'updation_lines':total_lines
        })
        days = 0
        total_hours = 0.00
        employee_id = None
        task_id = None
        months = None
        total_lines = []
        # self.updation_lines = None
        for timsheet in self.timesheet_ids.filtered(lambda a: a.date.month == 2):
            # if month == 1:
            months = '02'
            employee_id = timsheet.employee_id.id
            task_id = self.name
            days += 1
            if timsheet.unit_amount > 0.00:
                total_hours += timsheet.unit_amount
            else:
                total_hours += timsheet.overtime_amt
        lines = (0, 0, {
            'month': months,
            'employee_id': employee_id,
            'task_id': task_id,
            'days': days,
            'total_hours_per_month': total_hours,
        })
        print("lines",lines)
        if total_hours != 0.00:

            total_lines.append(lines)
        self.update({
            'updation_lines': total_lines
        })
        days = 0
        total_hours = 0.00
        employee_id = None
        task_id = None
        months = None
        total_lines = []
        # self.updation_lines = None
        for timsheet in self.timesheet_ids.filtered(lambda a: a.date.month == 3):
            # if month == 1:
            months = '03'
            employee_id = timsheet.employee_id.id
            task_id = self.name
            days += 1
            if timsheet.unit_amount > 0.00:
                total_hours += timsheet.unit_amount
            else:
                total_hours += timsheet.overtime_amt

        lines = (0, 0, {
            'month': months,
            'employee_id': employee_id,
            'task_id': task_id,
            'days': days,
            'total_hours_per_month': total_hours,
        })
        print("lines",lines)
        if total_hours != 0.00:

                total_lines.append(lines)
        self.update({
            'updation_lines': total_lines
        })
        days = 0
        total_hours = 0.00
        employee_id = None
        task_id = None
        months = None
        total_lines = []
        # self.updation_lines = None
        for timsheet in self.timesheet_ids.filtered(lambda a: a.date.month == 4):
            # if month == 1:
            months = '04'
            employee_id = timsheet.employee_id.id
            task_id = self.name
            days += 1
            if timsheet.unit_amount > 0.00:
                total_hours += timsheet.unit_amount
            else:
                total_hours += timsheet.overtime_amt

        lines = (0, 0, {
            'month': months,
            'employee_id': employee_id,
            'task_id': task_id,
            'days': days,
            'total_hours_per_month': total_hours,
        })
        print("lines",lines)
        if total_hours != 0.00:

            total_lines.append(lines)
        self.update({
            'updation_lines': total_lines
        })

        days = 0
        total_hours = 0.00
        employee_id = None
        task_id = None
        months = None
        total_lines = []
        # self.updation_lines = None
        for timsheet in self.timesheet_ids.filtered(lambda a: a.date.month == 5):
            # if month == 1:
            months = '05'
            employee_id = timsheet.employee_id.id
            task_id = self.name
            days += 1
            if timsheet.unit_amount > 0.00:
                total_hours += timsheet.unit_amount
            else:
                total_hours += timsheet.overtime_amt
        lines = (0, 0, {
            'month': months,
            'employee_id': employee_id,
            'task_id': task_id,
            'days': days,
            'total_hours_per_month': total_hours,
        })
        if total_hours != 0.00:

            total_lines.append(lines)
        self.update({
            'updation_lines':total_lines
        })
        days = 0
        total_hours = 0.00
        employee_id = None
        task_id = None
        months = None
        total_lines = []
        # self.updation_lines = None
        for timsheet in self.timesheet_ids.filtered(lambda a: a.date.month == 6):
            # if month == 1:
            months = '06'
            employee_id = timsheet.employee_id.id
            task_id = self.name
            days += 1
            if timsheet.unit_amount > 0.00:
                total_hours += timsheet.unit_amount
            else:
                total_hours += timsheet.overtime_amt
        lines = (0, 0, {
            'month': months,
            'employee_id': employee_id,
            'task_id': task_id,
            'days': days,
            'total_hours_per_month': total_hours,
        })
        if total_hours != 0.00:

            total_lines.append(lines)
        self.update({
            'updation_lines':total_lines
        })
        days = 0
        total_hours = 0.00
        employee_id = None
        task_id = None
        months = None
        total_lines = []
        # self.updation_lines = None
        for timsheet in self.timesheet_ids.filtered(lambda a: a.date.month == 7):
            # if month == 1:
            months = '07'
            employee_id = timsheet.employee_id.id
            task_id = self.name
            days += 1
            if timsheet.unit_amount > 0.00:
                total_hours += timsheet.unit_amount
            else:
                total_hours += timsheet.overtime_amt

        lines = (0, 0, {
            'month': months,
            'employee_id': employee_id,
            'task_id': task_id,
            'days': days,
            'total_hours_per_month': total_hours,
        })
        if total_hours != 0.00:

            total_lines.append(lines)
        self.update({
            'updation_lines': total_lines
        })
        days = 0
        total_hours = 0.00
        employee_id = None
        task_id = None
        months = None
        total_lines = []
        # self.updation_lines = None
        for timsheet in self.timesheet_ids.filtered(lambda a: a.date.month == 8):
            # if month == 1:
            months = '08'
            employee_id = timsheet.employee_id.id
            task_id = self.name
            days += 1
            if timsheet.unit_amount > 0.00:
                total_hours += timsheet.unit_amount
            else:
                total_hours += timsheet.overtime_amt

        lines = (0, 0, {
            'month': months,
            'employee_id': employee_id,
            'task_id': task_id,
            'days': days,
            'total_hours_per_month': total_hours,
        })
        if total_hours != 0.00:

            total_lines.append(lines)
        self.update({
            'updation_lines': total_lines
        })
        days = 0
        total_hours = 0.00
        employee_id = None
        task_id = None
        months = None
        total_lines = []
        # self.updation_lines = None
        for timsheet in self.timesheet_ids.filtered(lambda a: a.date.month == 9):
            # if month == 1:
            months = '09'
            employee_id = timsheet.employee_id.id
            task_id = self.name
            days += 1
            if timsheet.unit_amount > 0.00:
                total_hours += timsheet.unit_amount
            else:
                total_hours += timsheet.overtime_amt

        lines = (0, 0, {
            'month': months,
            'employee_id': employee_id,
            'task_id': task_id,
            'days': days,
            'total_hours_per_month': total_hours,
        })
        if total_hours != 0.00:

            total_lines.append(lines)
        self.update({
            'updation_lines': total_lines
        })
        days = 0
        total_hours = 0.00
        employee_id = None
        task_id = None
        months = None
        total_lines = []
        # self.updation_lines = None
        for timsheet in self.timesheet_ids.filtered(lambda a: a.date.month == 10):
            # if month == 1:
            months = '10'
            employee_id = timsheet.employee_id.id
            task_id = self.name
            days += 1
            if timsheet.unit_amount > 0.00:
                total_hours += timsheet.unit_amount
            else:
                total_hours += timsheet.overtime_amt

        lines = (0, 0, {
            'month': months,
            'employee_id': employee_id,
            'task_id': task_id,
            'days': days,
            'total_hours_per_month': total_hours,
        })
        if total_hours != 0.00:

            total_lines.append(lines)
        self.update({
            'updation_lines': total_lines
        })
        days = 0
        total_hours = 0.00
        employee_id = None
        task_id = None
        months = None
        total_lines = []
        # self.updation_lines = None
        for timsheet in self.timesheet_ids.filtered(lambda a: a.date.month == 11):
            # if month == 1:
            months = '11'
            employee_id = timsheet.employee_id.id
            task_id = self.name
            days += 1
            if timsheet.unit_amount > 0.00:
                total_hours += timsheet.unit_amount
            else:
                total_hours += timsheet.overtime_amt

        lines = (0, 0, {
            'month': months,
            'employee_id': employee_id,
            'task_id': task_id,
            'days': days,
            'total_hours_per_month': total_hours,
        })
        if total_hours != 0.00:

            total_lines.append(lines)
        self.update({
            'updation_lines': total_lines
        })
        days = 0
        total_hours = 0.00
        employee_id = None
        task_id = None
        months = None
        total_lines = []
        # self.updation_lines = None
        for timsheet in self.timesheet_ids.filtered(lambda a: a.date.month == 12):
            # if month == 1:
            months = '03'
            employee_id = timsheet.employee_id.id
            task_id = self.name
            days += 1
            if timsheet.unit_amount > 0.00:
                total_hours += timsheet.unit_amount
            else:
                total_hours += timsheet.overtime_amt

        lines = (0, 0, {
            'month': months,
            'employee_id': employee_id,
            'task_id': task_id,
            'days': days,
            'total_hours_per_month': total_hours,
        })
        if total_hours != 0.00:

            total_lines.append(lines)
        self.update({
            'updation_lines': total_lines
        })












    # def onchange_updation_lines(self):
    #     # employee_id = None
    #     # total_hours = 0.00
    #     # task_id = None
    #     # days = 0
    #     # total_list = []
    #     # month = None
    #     # self.updation_lines = None
    #     # for timesheet in self.timesheet_ids:
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         total_list = []
    #         month = None
    #         self.updation_lines = None
    #
    #         # if timesheet.date:
    #         #     month = timesheet.date.month
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 1):
    #             month = "01"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             print("task_id",task_id)
    #
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line",line)
    #
    #         total_list.append(line)
    #         self.update({
    #             'updation_lines': total_list
    #         })
    #
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         total_list = []
    #         month = None
    #         # self.updation_lines = None
    #
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 2):
    #             month = "02"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             print("task_id", task_id)
    #
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line", line)
    #
    #         total_list.append(line)
    #         self.update({
    #             'updation_lines': total_list
    #         })
    #
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         total_list = []
    #         month = None
    #         # self.updation_lines = None
    #
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 5):
    #             month = "05"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             print("task_id",task_id)
    #
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line", line)
    #
    #         total_list.append(line)
    #         self.update({
    #             'updation_lines': total_list
    #         })
    #
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         total_list = []
    #         month = None
    #         # self.updation_lines = None
    #
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 6):
    #             month = "06"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             print("task_id", task_id)
    #
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line", line)
    #
    #         total_list.append(line)
    #         self.update({
    #             'updation_lines': total_list
    #         })







    # @api.onchange('timesheet_ids')
    # def onchange_updation_lines(self):
    #     # total_list = []
    #     # month = None
    #     # self.updation_lines = None
    #     total_list = []
    #
    #     for timesheet in self.timesheet_ids:
    #         total_list = []
    #         month = None
    #
    #         self.updation_lines = None
    #         if timesheet.date:
    #             month = timesheet.date.month
    #             print('timesheet.date', month)
    #
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         total_list = []
    #
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 1):
    #             month = "01"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             print("task_id",task_id)
    #
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line",line)
    #             total_list.append(line)
    #         self.update({
    #             'updation_lines': total_list
    #         })
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 2):
    #             month = "02"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line", line)
    #             total_list.append(line)
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 3):
    #             month = "03"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line", line)
    #
    #             total_list.append(line)
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 4):
    #             month = "04"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line", line)
    #
    #             total_list.append(line)
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         total_list = []
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 5):
    #             month = "05"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line", line)
    #
    #             total_list.append(line)
    #         self.update({
    #             'updation_lines': total_list
    #         })
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         total_list = []
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 6):
    #             month = "06"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line",line)
    #
    #             total_list.append(line)
    #         self.update({
    #             'updation_lines': total_list
    #         })
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 7):
    #             month = "07"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line", line)
    #
    #             total_list.append(line)
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 8):
    #             month = "08"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line", line)
    #
    #             total_list.append(line)
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 9):
    #             month = "09"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line", line)
    #
    #             total_list.append(line)
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 10):
    #             month = "10"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line", line)
    #
    #             total_list.append(line)
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 11):
    #             month = "11"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line", line)
    #
    #             total_list.append(line)
    #         employee_id = None
    #         total_hours = 0.00
    #         task_id = None
    #         days = 0
    #         for time in self.timesheet_ids.filtered(lambda a: a.date.month == 12):
    #             month = "12"
    #             employee_id = time.employee_id.id
    #             task_id = self.name
    #             days += 1
    #             if time.unit_amount > 0.00:
    #                 total_hours += time.unit_amount
    #             else:
    #                 total_hours += time.overtime_amt
    #
    #             line = (0, 0, {
    #                 'month': month,
    #                 'employee_id': employee_id,
    #                 'task_id': task_id,
    #                 'days': days,
    #                 'total_hours_per_month': total_hours,
    #
    #             })
    #             print("line", line)
    #
    #             total_list.append(line)
    #         self.update({
    #             'updation_lines': total_list
    #         })



class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    overtime_amt = fields.Float('Overtime Amount')
    normal_hour = fields.Float('Normal Hour')
    weekend_or_holiday = fields.Boolean('Weekend/Holiday')
    month = fields.Selection([('01','January'),('02','February'),('03','March'),('04','April'),('05','May'),('06','June'),('07','July'),('08','August'),('09','September'),('10','October'),('11','November'),('12','December')],string='Month')
    # month = fields.Char('Month')



    @api.onchange('date')
    def onchange_month(self):
        print(self.date.month)
        if self.date.month == 1:
            self.month = '01'
        if self.date.month == 2:
            self.month = '02'
        if self.date.month == 3:
            self.month = '03'
        if self.date.month == 4:
            self.month = '04'
        if self.date.month == 5:
            self.month = '05'
        if self.date.month == 6:
            self.month = '06'
        if self.date.month == 7:
            self.month = '07'
        if self.date.month == 8:
            self.month = '08'
        if self.date.month == 9:
            self.month = '09'
        if self.date.month == 10:
            self.month = '10'
        if self.date.month == 11:
            self.month = '11'
        if self.date.month == 12:
            self.month = '12'






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



class TimesheetUpdationLines(models.Model):
    _name = 'timesheet.updation.lines'


    month = fields.Selection([('01','January'),('02','February'),('03','March'),('04','April'),('05','May'),('06','June'),('07','July'),('08','August'),('09','September'),('10','October'),('11','November'),('12','December')],string='Month')
    employee_id = fields.Many2one('hr.employee',string='Employee')
    # task_id = fields.Many2one('project.task',string='Task')
    task_id = fields.Char(string='Task')
    days = fields.Char(string='Days')
    total_hours_per_month = fields.Float('Total Hours Per Month')
    timesheet_lines = fields.Many2one('project.task')



