function client() {
    this.upload = new Generic();
    this.init();
}

client.prototype.init = function() {
    this.setDefaultProps();
    this.toggleClient();
    this.createClient();
    this.validateClientFrm();
};

client.prototype.setDefaultProps = function() {
    // $('#btn_newClient').attr('disabled','disabled');
    $('#errorAlert').hide(true);
};
client.prototype.toggleClient = function() {
    $('#client_toggle').click(function() {
        $("#new_client").toggle()
    });
};

client.prototype.createClient = function() {
    self = this;
    $('#btn_newClient').click(function() {
        var data = JSON.stringify({
            fullname: $('#fullname').val(),
            phone_number: $('#phone_number').val(),
            email: $('#email').val(),
            address1: $('#address1').val(),
        });
        self.upload.ajaxCall('/clients','POST', data, function(err,response) {
            if (err !== undefined && err !== null) {
                // handle error
            } else {
                if (response.isSuccessful) {
                    // handle success
                } else {
                    // handle response
                }
            }
        })
    });
};

client.prototype.validateClientFrm = function() {
    // use form dirt to validate form in jquery
    $('form[id="frm_client"]').validate({
        rules: {
            fullname: 'required',
            phone_number: 'required',
            email: {
              required: true,
              email: true,
            },
            address1: {
              required: true,
              minlength: 8,
            }
          },
          messages: {
            fullname: 'This field is required',
            phone_number: 'This field is required',
            email: 'Enter a valid email',
            address1: {
              minlength: 'Address must be at least 5 characters long'
            }
          },
          submitHandler: function(form) {
            // $('#btn_newClient').removeAttr('disabled','disabled');
            form.submit();
        }
    });
};