var app = angular.module("HighlightApp", []);

app.controller('EntryController', function() {
    this.filename   = '';
    this.code       = '';

    this.change = function() {
        $httpProvider.defaults.headers.get = {Content-Type: application/json};
        var req = $http({
                method: 'GET',
                url: '/api/v0.1/highlight',
                data: {
                    filename: this.filename,
                    code: this.code,
                },
        }).then(function successCallback(response) {
            var data    = response.data;
            if(data.success == true) {
                this.code = data.code;
            }
        }, function errorCallback(response) {

        });
    };
});
