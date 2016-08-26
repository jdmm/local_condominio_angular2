# -*- coding: utf-8 -*-
{
    'name': "Siscond Owner",

    'summary': """
        module for recording owners""",

    'description': """
        Modulo de propietarios para el Sistema de Condominio
    """,

    'author': "JPV(Jonathan Jose Reyes Veliz).",
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
        'views/siscond_owners_views.xml',
        'security/siscond_role.xml',
    ],
 
}