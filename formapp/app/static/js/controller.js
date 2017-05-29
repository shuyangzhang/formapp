var app = angular.module('formapp', []);
app.controller('formctrl', ['$scope', '$http', function($scope, $http){
	$scope.master = {
		// name:"zhangshuyang",
		// placeRadio:1,
		// placetyped:"清华大学图书馆",
		// beforeAction:1,
		// jacket:1,
		// trousers:1,
		// temperature:1,
		// confortable:1,
		// totalconf:1,
		// beats:90,
		// lon:100,
		// lat:100
	};
	$scope.create_form = function(){
		if (!$scope.master.beats){
			$scope.master.beats=0;
		}
		$http.post('http://127.0.0.1:8000/act/sign', $scope.master).success(function(data){
			alert('感谢您参与问卷！');
		});
	};
 	$scope.nearme = function() {
	    
	        // navigator.geolocation.getCurrentPosition();
	        navigator.geolocation.getCurrentPosition(function (position) {

	                $scope.master.lat = position.coords.latitude; 
	                $scope.master.lon = position.coords.longitude;
	        });

	       
	    
	}

	// $scope.nearme = function(){
	
	// }	
}]);
