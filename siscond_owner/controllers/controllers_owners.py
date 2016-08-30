# -*- coding: utf-8 -*-

import openerp
from openerp.addons.base.ir.ir_qweb import AssetsBundle
from openerp.addons.web.controllers.main import WebClient, Binary
from openerp.addons.web import http
from openerp.http import request

class SiscondOwners(http.Controller):

	@http.route('/siscond/owners/massivedownloadformat', type='http', auth="public", website=True)
   	def massivedownloadformat(self, **kw):
		templateId='siscond_owner.massive_download_format_owners'
		values={
    		'hola':'hola'	
    		}
		return request.render(templateId, values)
  