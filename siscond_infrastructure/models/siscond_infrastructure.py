# -*- coding: utf-8 -*-

from openerp import models, fields, api

class siscond_infrastructure(models.Model):
    _name = 'siscond_infrastructure.infrastructure'

    name = fields.Char('Nombre', help='Por favor, ingrese el nombre de la  infraestructura')
    contract_id = fields.Many2one('sis_cond.registro_contrato',
                                        'Contrato',
                                        ondelete="cascade"
                                        )
    company_id = fields.Many2one("res.company", related="contract_id.company_id", string="Compañia", readonly=True)
    tower_ids = fields.One2many('siscond_infrastructure.tower', 'infrastructure_id', 'Towers Line')
    property_commons_line_ids = fields.One2many('siscond_infrastructure.property_common_line', 'infrastructure_id', 'Property Commons Line')
    active = fields.Boolean('Active', default=True)
    
    

class siscond_tower(models.Model):
    _name = 'siscond_infrastructure.tower'
    _recname = 'name'


    name = fields.Char('Nombre', help='Por favor, ingrese el nombre de la torre')
    infrastructure_id = fields.Many2one('siscond_infrastructure.infrastructure',
                                        'Infraestructura',
                                        ondelete="cascade"
                                        )
    property_commons_line_ids = fields.One2many('siscond_infrastructure.property_common_line', 'tower_id', 'Property Commons Line')
    floor_ids = fields.One2many('siscond_infrastructure.floor','tower_id', 'Registro de pisos')
    active = fields.Boolean('Active', default=True)
    
    
    

class siscond_floor(models.Model):
    _name = 'siscond_infrastructure.floor'

    name = fields.Char('Nombre', help='Por favor, ingrese el nombre del piso')
    tower_id = fields.Many2one('siscond_infrastructure.tower', 'Torre', ondelete="cascade")
    active = fields.Boolean('Active', default=True)
    property_ids = fields.One2many('siscond_infrastructure.property','floor_id', 'Registro de Propiedades')

    


class siscond_property_common(models.Model):
    _name = 'siscond_infrastructure.property_common'


    name = fields.Char('Nombre', help='Please enter the name of the property common')
    description = fields.Char('Descripcion', help='Please enter the name of the property common')
    # capacity=fields.Char('Capacidad')
    active = fields.Boolean('Active', default=True)


class siscond_property_common_line(models.Model):
    _name = 'siscond_infrastructure.property_common_line'


    property_common_id= fields.Many2one('siscond_infrastructure.property_common', 'Tipo de Propiedad Comun')
    description = fields.Char('Descripcion', help='Please enter the name of the property common')
    infrastructure_id = fields.Many2one('siscond_infrastructure.infrastructure',
                                        'Infrastructure',
                                        ondelete="cascade"
                                        )
    # capacity=fields.Char('Capacidad')
    tower_id = fields.Many2one('siscond_infrastructure.tower', 'Tower', ondelete="cascade")
    active = fields.Boolean('Active', default=True)

   




class siscond_property(models.Model):
    _name = 'siscond_infrastructure.property'


    name = fields.Char('Nombre', help='Please enter the name of the property')
    floor_id = fields.Many2one('siscond_infrastructure.floor',
                                        'Floor',
                                        ondelete="cascade") 

    type_property_id = fields.Many2one('siscond_infrastructure.type_property',
                                        'Tipo de Propiedad',
                                        ondelete="cascade")

    owner_ids=fields.Many2many('res.partner','partner_property_rel', 'property_id', 'partner_id', 'Propietarios')

    aliquot = fields.Float('Alicuota')
    active = fields.Boolean('Active', default=True)


    

class siscond_type_property(models.Model):
    _name = 'siscond_infrastructure.type_property'


    name = fields.Char('Nombre', help='Please enter the name of the type property', secuence=1)
    description = fields.Char('Descripción', help='Please enter the name of the type property')

    active = fields.Boolean('Active', default=True)