odoo.define('siscond_owner.orm', function (require) {
"use strict";
var core = require('web.core');
var base = require('web_editor.base');
var website = require('website.website');
var Model = require('web.Model');
var towerObj = new Model('siscond_infrastructure.tower');

angular
    .module('MyfirstApp')
    .controller('SelectedTowers', function($timeout,$scope,$mdDialog) {
	$scope.tower=undefined;
	$scope.towers=null;
      $scope.loadTowers = function() {
		return $timeout(function() {
      $scope.towers = $scope.towers  || [];
      if (!$scope.towers.length){
          towerObj.call('search_towers',['',[1,2,3,4]],
                  {context:base.get_context()}).then(function (result) {
          $scope.towers = $scope.towers  || [];
          for(var i=0;i<result.length;i++) {
			$scope.towers.push({ id: result[i][0], name: result[i][1] });
          }
        });
		}
	});
	};
	
	$scope.getSelectedText = function() {
		if ($scope.tower !== undefined) {
		  return "Usted ha selecionado: Torre " + $scope.tower.name;
		}else {
		  return "Torres";
		}}
		
	
	$scope.dowloadExcel = function(ev) {
		if ($scope.tower !== undefined){
			var towerId=$scope.tower.id
			  console.log(towerId)
			  console.log(towerId)
			  console.log(99999)
			  console.log(99999)
			}else{
				$mdDialog.show(
				  $mdDialog.alert()
					.clickOutsideToClose(true)
					.title('Aviso!')
					.textContent('Seleccione una Torre.')
					.ariaLabel('Alert Dialog Demo')
					.ok('Cerrar')
					.targetEvent(ev)
				);
				}
    };
		
		
    });
});

  
