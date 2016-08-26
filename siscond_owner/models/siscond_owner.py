# -*- coding: utf-8 -*-

from openerp import models, fields, api, _
from openerp.exceptions import UserError
import re

class res_partner(models.Model):
    _inherit = 'res.partner'

    owner = fields.Boolean('Propietario', defaults=False)
    identity_card = fields.Char('Cedula', help='Porfavor ingrese su numero de cédula')
    rif = fields.Char('RIF', help='Porfavor ingrese el RIF')
    property_ids=fields.Many2many('siscond_infrastructure.property','partner_property_rel', 'partner_id', 'property_id', readonly=True)

    _sql_constraints = [
            ('identity_card_unique', 'unique(identity_card)', 'Ya existe un propietario con la cédula que usted ha indicado'),
            ('rif_unique', 'unique(rif)', 'Ya existe un propietario con el RIF que usted ha indicado'),
            ]

class res_users(models.Model):
    _inherit = 'res.users'

    @api.multi
    def validate_email(self,vals):
        login = vals['login'].strip()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", login):
            raise UserError(_(u'''Formato de correo incorrecto.\n %s  ''' % (login)))
        return

    @api.multi
    def on_change_groups_defaults(self,groups_id):
        groups_ids = self.env['res.groups'].search([('name','=','Propietario')])
        if groups_ids:
            groups_id.append((groups_ids[0].id))
        return {'value': {'groups_id': groups_id}}

    @api.multi
    def on_change_owner_defaults(self):
        return {'value': {'owner': True}}

    @api.multi
    def on_change_is_company(self,is_company):
        return {'value': {'identity_card': '','rif':''}}

    @api.model
    def create(self, vals):
        self.validate_email(vals)
        owner_id = super(res_users, self).create(vals)
        return owner_id

    @api.multi
    def write(self, vals):
        if 'email' in vals.keys():
            self.validate_email(vals)
        result = super(res_users, self).write(vals)
        return result

