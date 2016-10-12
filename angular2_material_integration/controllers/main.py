# -*- coding: utf-8 -*-

from openerp import http
from openerp.addons.web.controllers import main
from openerp import SUPERUSER_ID
from openerp.addons.web.http import request
from openerp.addons.website_blog.controllers import main as main_blog

QueryURL=main_blog.QueryURL
class index(main.Home):
    @http.route('/', auth='public', website=True)
    def index(self):
        return http.request.website.render('angular_material_integration.layout_angular_material', {'edit':False
        })


    @http.route('/name_search/select', auth='public', website=True)
    def name_search(self,**post):

        
        return http.request.website.render('angular_material_integration.layout_angular_material', {'edit':False
        })