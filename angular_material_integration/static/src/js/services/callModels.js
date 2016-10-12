odoo.define('angular_material_integration.callModels', function (require) {
"use strict";
	var core = require('web.core');
	var base = require('web_editor.base');
	var website = require('website.website');
	var Model = require('web.Model');

	var app = angular.module("MyfirstApp");
	app.factory('callModels',function($scope){

		
		
		callModels.call = function(modelName,idModel){
			console.log('ejecutando servicion');
			var Obj = new Model(modelName);
			Obj.call('search_towers',['',idModel],
	                  {context:base.get_context()}).then(function (result) {
	          return result;
	          });
	            return callModels;
	        };

	   

		});

});