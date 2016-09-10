odoo.define('angular_material_integration.orm', function (require) {
"use strict";

var core = require('web.core');
var base = require('web_editor.base');
var Model = require('web.Model');
var website = require('website.website');
var users = new Model('res.users');

  

  return {
  	user_name_search:function(){

  		return users.call('name_search', ['', [['public','=','public']]],
                  {context: some_context});
  	} 
  }
  
  });

console.log(odoo.services);