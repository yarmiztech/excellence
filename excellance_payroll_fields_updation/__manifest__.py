{
    'name': "Excellance Payroll Fields Updation",
    'author':
        'ENZAPPS',
    'summary': """
This module is for Excellance HR Updation.
""",

    'description': """
        This module is for Excellance HR Updation.
    """,
    'website': "",
    'category': 'base',
    'version': '14.0',
    'depends': ['base', 'account', 'stock', 'product', 'sale_management', 'purchase', 'crm', 'contacts', 'hr',
                'hr_contract', 'hr_timesheet', 'project', 'hr_expense', 'analytic', 'hr_recruitment', 'om_hr_payroll',
                'enz_manpower','enz_manpower_overtime','om_hr_payroll_account','excellance','alhokair_einvoice_reports',
                'excellence_einvoice','excellence_invoice_updation','excellence_corrections','excellance_sale_updation',
                'excellance_hr_updation','excellence_new_structure','excellance_sale_wizard_corrections',],
    "images": ['static/description/icon.png'],
    'data': [
        'security/project_task_security.xml',
        'security/ir.model.access.csv',
        'views/inherit_hr_payslip.xml',
        'views/inherit_hr_payslip_printout.xml',
        # 'views/inherit_account_analytic_line.xml',
        'views/project_task.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}
