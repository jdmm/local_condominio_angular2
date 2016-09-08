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

      $scope.users =  $scope.users  || [
        { id: 1, name: 'Scooby Doo' },
        { id: 2, name: 'Shaggy Rodgers' },
        { id: 3, name: 'Fred Jones' },
        { id: 4, name: 'Daphne Blake' },
        { id: 5, name: 'Velma Dinkley' }
      ];

    }, 650);
  };
    }); 