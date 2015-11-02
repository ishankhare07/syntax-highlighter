var app = angular.module("HighlightApp", ['ngSanitize']);

app.controller('EntryController', ['$http', function($http) {
    this.filename           = '';
    this.code               = '';
    this.highlighted_code   = '';

    this.change = function() {
        console.log("executing function");
        var req = $http({
                method: 'POST',
                url: '/api/v0.1/highlight',
                data: {
                    filename: this.filename,
                    code: this.code,
                },
        }).then(function successCallback(response) {
            var data    = response.data;
            if(data.success == true) {
                console.log(data.highlighted_code);
                //connect stylesheet
                if(document.getElementById('highlight_css_' + data.id_name) == null) {
                    var style_element = document.createElement('link');
                    style_element.setAttribute('rel', 'stylesheet');
                    style_element.setAttribute('href', window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/' + data.css_class);
                    style_element.setAttribute('id', 'highlight_css_' + data.id_name);
                    document.head.appendChild(style_element);
                }
                var element = angular.element(document.querySelector('#background'));
                element.html(data.highlighted_code);
            }
        }, function errorCallback(response) {
            'pass';
        });
    };
}]);
