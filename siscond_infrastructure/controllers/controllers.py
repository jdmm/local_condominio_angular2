# -*- coding: utf-8 -*-
from openerp import http

# class SiscondInfraestructure(http.Controller):
#     @http.route('/siscond_infraestructura/siscond_infraestructura/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/siscond_infraestructura/siscond_infraestructura/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('siscond_infraestructura.listing', {
#             'root': '/siscond_infraestructura/siscond_infraestructura',
#             'objects': http.request.env['siscond_infraestructura.siscond_infraestructura'].search([]),
#         })

#     @http.route('/siscond_infraestructura/siscond_infraestructura/objects/<model("siscond_infraestructura.siscond_infraestructura"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('siscond_infraestructura.object', {
#             'object': obj
#         })