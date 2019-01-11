function app() {
    this.upload = new Generic();
    this.init();
}

app.prototype.init = function() {
    this.setDefaultProps();
    this.toggleClient();
    this.createClient();
    this.validateClientFrm();
};

app.prototype.toggleClient = function() {
    $('#client_toggle').click(function() {
        $("#new_client").toggle()
    });
};
app.prototype.setDefaultProps = function() {
    // $('#btn_newClient').attr('disabled','disabled');
    $('#errorAlert').hide(true);
};
app.prototype.createClient = function() {
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

            } else {
                if (response.isSuccessful) {
                } else {
                }
            }
        })
    });
};
app.prototype.validateClientFrm = function() {
    // use form dirt to validate form in jquery
    $('form[id="frm_client"]').validate({
        rules: {
            full_name: 'required',
            phone_number: 'required',
            email_address: {
              required: true,
              email: true,
            },
            office_address: {
              required: true,
              minlength: 8,
            }
          },
          messages: {
            full_name: 'This field is required',
            phone_number: 'This field is required',
            email_address: 'Enter a valid email',
            office_address: {
              minlength: 'Address must be at least 5 characters long'
            }
          },
          submitHandler: function(form) {
            // $('#btn_newClient').removeAttr('disabled','disabled');
            form.submit();
        }
    });
};