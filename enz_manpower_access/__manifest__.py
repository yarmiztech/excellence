# -*- coding: utf-8 -*-
{
    'name': "Enzapps Man Power Access",
    'author':
        'ENZAPPS',
    'summary': """
This module is for Enzapps Man Power Access.
""",

    'description': """
        This module is for Enzapps Man Power Access.
    """,
    'website': "",
    'category': 'base',
    'version': '12.0',
    'depends': ['base', 'account', 'stock', 'product', 'sale_management', 'purchase', 'crm', 'contacts', 'hr',
                'hr_contract', 'hr_timesheet', 'project', 'hr_expense', 'analytic', 'hr_recruitment', 'om_hr_payroll',
                'enz_manpower','enz_manpower_overtime','om_hr_payroll_account','excellance','alhokair_einvoice_reports',
                'excellence_einvoice','excellence_invoice_updation','excellence_corrections','excellance_sale_updation',
                'excellance_hr_updation','excellence_new_structure','excellance_sale_wizard_corrections','excellance_payroll_fields_updation'],
    "images": ['static/description/icon.png'],
    'data': [
        # 'data/record_rule.xml',
        'data/security.xml',
        'views/menus.xml',
        'views/inherit_payslip.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}
