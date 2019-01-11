function Generic() {
    this.init();
}

Generic.prototype.init = function (){
}

Generic.prototype.ajaxCall = function(url, verb, _data, callback) {
    var csrftoken = $('input[name=_csrf_token]').attr('value');
    $.ajax({
        type: verb,
        url: url,
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: _data,
        beforeSend: function(xhr, settings) {
            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                console.log(csrftoken);
                xhr.setRequestHeader("X-CSRFToken", csrftoken)
                
            }
        },
        success: function (response) {
            callback(null, response);
        },
        error: function (xhr, ajaxOptions, thrownError) {
            callback("Failed to process request", null);
        }
    });
}