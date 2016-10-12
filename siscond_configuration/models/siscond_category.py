# -*- coding: utf-8 -*-

from openerp import models, fields, api

class siscond_category(models.Model):
    _name = 'siscond_category.category'

    category = fields.Char('Nombre', help='Por favor, ingrese el nombre'\
                            'para la categoría de gastos.',
                            require=True,
                            )
    contract_id = fields.Many2one('sis_cond.registro_contrato',
                            'Contrato',
                            ondelete="restrict",
                            )
    company_id = fields.Many2one("res.company", 
                            related="contract_id.company_id", 
                            string="Compañía", 
                            readonly=False,
                            )
    property_ids = fields.Many2many("siscond_infrastructure.property", 
                            'category_property_rel', 
                            'category_id', 
                            'property_id', 
                            'Propiedades',
                            )
    active = fields.Boolean('Active', 
                            default=True,
                            )
    
    

