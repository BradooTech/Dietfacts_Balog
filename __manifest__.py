# -*- coding: utf-8 -*-
{
'name': "dietfacts",

'summary': """
Short (1 phrase/line) summary of the module's purpose, used as
subtitle on modules listing or apps.openerp.com""",

'description': """
Informations about calories, etc
""",

'author': "My Company",
'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    'installable': True,

    # any module necessary for this one to work correctly
    'depends': ['sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/actions.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/dietfacts_view.xml',
        'security/ir.model.access.csv',
        'reports/product.nutrition_report.xml',
        'reports/product.nutrition_report_template.xml'
        ],
    # only loaded in demonstration mode
    'demo': [
    'demo/demo.xml',
    ],
    }
