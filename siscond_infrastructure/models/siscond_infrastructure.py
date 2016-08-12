# -*- coding: utf-8 -*-

from openerp import models, fields, api

class siscond_infrastructure(models.Model):
    _name = 'siscond_infrastructure.infrastructure'

    name = fields.Char('Name', help='Please enter the name of the infraestructure')
    tower_ids = fields.One2many('siscond_infrastructure.tower', 'infrastructure_id', 'Towers Line')
    active = fields.Boolean('Active', defaults=True)
    
    

class siscond_tower(models.Model):
    _name = 'siscond_infrastructure.tower'
    _recname = 'name'


    name = fields.Char('Name', help='Please enter the name of the tower')
    infrastructure_id = fields.Many2one('siscond_infrastructure.infrastructure',
                                        'Infrastructure'
                                        )
    floor_ids = fields.One2many('siscond_infrastructure.floor','tower_id', 'Floors Line')
    active = fields.Boolean('Active', defaults=True)
    
    
    

class siscond_floor(models.Model):
    _name = 'siscond_infrastructure.floor'

    name = fields.Char('Name', help='Please enter the name of the floor')
    tower_id = fields.Many2one('siscond_infrastructure.tower', 'Tower')
    active = fields.Boolean('Active', defaults=True)
    apartment_ids = fields.One2many('siscond_infrastructure.apartment','floor_id', 'Apartment Line')

    


class siscond_property_common(models.Model):
    _name = 'siscond_infrastructure.property_common'


    name = fields.Char('Name', help='Please enter the name of the property common')
    infrastructure_id = fields.Many2one('siscond_infrastructure.infrastructure',
                                        'Infrastructure'
                                        )
    active = fields.Boolean('Active', defaults=True)

   




class siscond_property(models.Model):
    _name = 'siscond_infrastructure.property'


    name = fields.Char('Name', help='Please enter the name of the property')
    floor_id = fields.Many2one('siscond_infrastructure.floor',
                                        'Floor'
                                        )
    owner_ids=fields.Many2many('res_partner','partner_property_rel', 'property_id', 'partner_id')

    aliquot = fields.Float('Aliquot')
    active = fields.Boolean('Active', defaults=True)


    

class siscond_apartment(models.Model):
    _name = 'siscond_infrastructure.apartment'
    _inherits = {'siscond_infrastructure.property' : 'property_id'}

    name = fields.Char('Name', help='Please enter the name of the apartment')
    floor_id = fields.Many2one('siscond_infrastructure.floor',
                                        'Floor'
                                        )
    property_id = fields.Many2one('siscond_infrastructure.property', 'Property')
    aliquot = fields.Float('Aliquot')
    active = fields.Boolean('Active', defaults=True)


    


class siscond_office(models.Model):
    _name = 'siscond_infrastructure.office'
    _inherits = {'siscond_infrastructure.property' : 'property_id'}


    name = fields.Char('Name', help='Please enter the name of the apartment')
    floor_id = fields.Many2one('siscond_infrastructure.floor',
                                        'Floor'
                                        )
    property_id = fields.Many2one('siscond_infrastructure.property', 'Property')
    aliquot = fields.Float('Aliquot')
    active = fields.Boolean('Active', defaults=True)

    

class siscond_premises(models.Model):
    _name = 'siscond_infrastructure.premises'
    _inherits = {'siscond_infrastructure.property' : 'property_id'}

    name = fields.Char('Name', help='Please enter the name of the apartment')
    floor_id = fields.Many2one('siscond_infrastructure.floor',
                                        'Floor'
                                        )
    property_id = fields.Many2one('siscond_infrastructure.property', 'Property')
    aliquot = fields.Float('Aliquot')
    active = fields.Boolean('Active', defaults=True)


