# -*- coding: utf-8 -*-

import openerp
from openerp.addons.base.ir.ir_qweb import AssetsBundle
from openerp.addons.web.controllers.main import WebClient, Binary
from openerp.addons.web import http
from openerp.http import request

class SiscondOwners(http.Controller):

	@http.route('/hola', type='http', auth="public", website=True)
   	def massivedownloadformat(self, **kw):
   		print ',mnmnjnkjnsdjnskjdnkjsndkjsnd'
   		print ',mnmnjnkjnsdjnskjdnkjsndkjsnd'
   		print ',mnmnjnkjnsdjnskjdnkjsndkjsnd'
   		print ',mnmnjnkjnsdjnskjdnkjsndkjsnd'
		templateId='siscond_owner.massive_download_format_owners'
		values={
    		'hola':'hola'	
    		}
		return request.render(templateId, values)
  