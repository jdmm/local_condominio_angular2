var app = angular.module("MySecondApp",['MyfirstApp']);
app.controller('SecondController',function ($scope) {
	$scope.apellido = "Mancilla";
});


// app.controller('SecondController', ['$scope', function ($scope) {
	
// }])
