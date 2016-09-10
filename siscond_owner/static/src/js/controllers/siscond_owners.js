odoo.define('siscond_owner.orm', function (require) {
"use strict";
var core = require('web.core');
var base = require('web_editor.base');
var website = require('website.website');
var Model = require('web.Model');
var users = new Model('res.users');
console.log(users);
angular
    .module('MyfirstApp')
    .controller('SelectedTextController', function($timeout,$scope) {
      $scope.items = [1, 2, 3, 4, 5, 6, 7];
      $scope.selectedItem;
      $scope.user = null;
      $scope.users = null;
      $scope.getSelectedText = function() {
        if ($scope.selectedItem !== undefined) {
          return "You have selected: Item " + $scope.selectedItem;
        } else {
          return "Please select an item";
        }
      };


      $scope.loadUsers = function() {

    // Use timeout to simulate a 650ms request.
    return $timeout(function() {

      $scope.users = $scope.users  || [];
      console.log($scope.users.length)
      if (!$scope.users.length){
          users.call('name_search',[],
                  {context:base.get_context()}).then(function (result) {
          console.log(result);
          $scope.users = $scope.users  || [];
          for(var i=0;i<result.length;i++) {
           $scope.users.push({ id: result[i][0], name: result[i][1] });
          }
          console.log( $scope.users)
          // $scope.users =  $scope.users  || [
          //   { id: 1, name: 'Scooby Doo' },
          //   { id: 2, name: 'Shaggy Rodgers' },
          //   { id: 3, name: 'Fred Jones' },
          //   { id: 4, name: 'Daphne Blake' },
          //   { id: 5, name: 'Velma Dinkley' }
          // ];
          console.log( $scope.users)
        // do something with change_password result
        });

      }
      
    });
  };
    });
   
});

  
