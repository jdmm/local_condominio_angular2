# -*- coding: utf-8 -*-
##############################################################################
#    
#    Modulo Desarrollado por Juventud Productiva (Victor Davila)
#    Visitanos en http://juventudproductivabicentenaria.blogspot.com/
#    Nuestro Correo juventudproductivabicentenaria@gmail.com
#
##############################################################################

{
    'name' : 'Registro de Contrato',
    'version' : '1.0',
    'summary': '',
    'sequence': 1,
    'description': """
Registro de Contrato
====================
Dentro de este Módulo se registraran los contratos que genere el sistema 
""",
    'category' : 'Registro de Contrato',
    'website': '',
    'images' : [],
    'depends' : ['base_setup', 'base'],
    'data': [
        'vistas/siscond_reg_contrato_v.xml',
    ],
    'demo': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}
