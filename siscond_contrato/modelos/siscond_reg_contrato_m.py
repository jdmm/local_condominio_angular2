# -*- coding: utf-8 -*-
##############################################################################
#    
#    Modulo Desarrollado por Juventud Productiva (Victor Davila)
#    Visitanos en http://juventudproductivabicentenaria.blogspot.com/
#    Nuestro Correo juventudproductivabicentenaria@gmail.com
#
##############################################################################

from openerp import api, fields, models, _

class RegistroContrato(models.Model):
    _name = 'sis_cond.registro_contrato'
    _inherits = {'res.company': 'company_id'}
    _description = "Registro de Contrato"
    
    rif = fields.Char(string='RIF', required=True, )
    cant_torre = fields.Integer('Cantidad de Torres', required=True,)
    cant_aptos = fields.Integer('Cantidad de Apartamentos', required=True,)
    cant_local = fields.Integer('Cantidad de Locales', required=True,)
    
    
