# -*- coding: utf-8 -*-
from openerp import http

# class SiscondInfraestructure(http.Controller):
#     @http.route('/siscond_configuration/siscond_configuration/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/siscond_configuration/siscond_configuration/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('siscond_configuration.listing', {
#             'root': '/siscond_configuration/siscond_configuration',
#             'objects': http.request.env['siscond_configuration.siscond_infraestructura'].search([]),
#         })

#     @http.route('/siscond_configuration/siscond_configuration/objects/<model("siscond_configuration.siscond_configuration"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('siscond_configuration.object', {
#             'object': obj
#         })
