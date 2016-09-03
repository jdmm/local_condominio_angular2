# -*- coding: utf-8 -*-
{
    'name': "Siscond Configuration",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Module configuration for the system condo...
    """,

    'author': "Jeison Pernía Araque",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','siscond_infrastructure'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/siscond_category_views.xml',
        #~ 'views/siscond_infrastructure_views.xml',
        #~ 'views/siscond_tower_views.xml',
        #~ 'views/siscond_floor_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
