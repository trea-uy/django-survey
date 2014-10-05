'use strict';

(function () {
	
    var app = angular.module('dynamicFormsFramework');
    
    /*
     * This controller handles the logic to display the list of forms
     */
    app.controller('MainPageCtrl', ['$scope','$http','$location', function ($scope, $http, $location) {
    	
    	var mainPage = this;
        mainPage.formSlugParam = ($location.search()).form;
        mainPage.versionIdParam = ($location.search()).ver;
        mainPage.orders = [
            {name: "Id", value: "id"},
            {name: "Owner", value: "owner"},
            {name: "Title", value: "title"},
            //{name: "Publish Date", value: "publish_date"},
        ];
        mainPage.ascdsc='asc';
        mainPage.selectascdsc = function(ascdsc) {
            mainPage.ascdsc = ascdsc;
        };
            
            
        $http.get('/dynamicForms/responses/'+mainPage.formSlugParam+'/'+ mainPage.versionIdParam+'/')
            .success(function(data){
                mainPage.json = data;
            })
            .error(function(data, status, headers, config){
               // alert('error cargando respuestas: ' + status);
            })
    }]);
})();
