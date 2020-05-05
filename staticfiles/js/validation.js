$( document ).ready(function() {
    /******* Common Email Format Validation - Starts here *********/
    jQuery.validator.addMethod("email", function(value, element) {
      // allow any non-whitespace characters as the host part
      return this.optional( element ) || /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/.test( value );
    }, 'Please enter a valid email address.');
    
    /******* Common Email Format Validation - Ends here *********/
    
    /******* Common Password Validation - Starts here *********/
    $.validator.addMethod("new_password1", function(value, element) {
        return this.optional(element) || /^[A-Za-z0-9\d=!\-@._*]+$/.test(value);
    }, "Please enter only alphabets or  numbers.");
     /******* Common Password Validation - Ends here *********/

// validation for Login Page starts here
    validator = $("#logn_form").validate({
        rules: {
            username: {
                required: true,
            },
             password: {
                 required: true,
                 //minlength: 6
             },
        },
        messages: {
            username: {
                required: "This field is required"
            },
            password: {
                 required: "This field is required",
                 //minlength: "Password should be atleast 6 characters",
            },
        },
    });
// validation for Login Page ends here


// validation for change Password starts here
    validator = $("#chang_pswd").validate({
        rules: {
            old_password: {
                required: true,
            },
             new_password1: {
                 required: true,
                 minlength: 6
             },
            new_password2: {
                required: true,
                equalTo : '#newpassword1'
            },
        },
        messages: {
            old_password: {
                required: "This field is required"
            },
             new_password1: {
                 required: "This field is required",
                 minlength: "Password should be atleast 6 characters",
             },
            new_password2: {
                required: "This field is required",
                equalTo : "Confirm Password should be same as New Password."
            },
        },
    });
// validation for change Password ends here

// validation for Reset password starts here
    validator = $("#reset_psw").validate({
        rules: {
             new_password1: {
                 required: true,
                 minlength: 6
             },
            new_password2: {
                required: true,
                equalTo : '#newpassword1'
            },
        },
        messages: {
             new_password1: {
                 required: "This field is required",
                 minlength: "Password should be atleast 6 characters",
             },
            new_password2: {
                required: "This field is required",
                equalTo : "Confirm Password should be same as New Password."
            },
        },
    });
// validation for Reset password  ends here

// validation for forgot Password starts here
    validator = $("#frgt_pswd").validate({
        rules: {
            email: {
                required: true,
            },
        },
        messages: {
            email: {
                required: "This field is required",
            },
        },
    });
// validation for forgot Password ends here

// slide show

$(".quick_links_block").ready(function() {
    $("#quickLinks").owlCarousel({
        autoPlay: 1000,loop: true,
        items : 1, // THIS IS IMPORTANT
        nav : true,
        dots : false,
        responsive : {
              480 : { items : 1  }, // from zero to 480 screen width 4 items
              768 : { items : 3  }, // from 480 screen widthto 768 6 items
              1024 : { items : 5   // from 768 screen width to 1024 8 items
              }
          },
    });
});

$(".logo_section_block").ready(function() {
    $("#logoSection").owlCarousel({
        autoPlay: 1000,
        loop: false,
        items : 1, // THIS IS IMPORTANT
        nav : true,
        dots : false,
        responsive : {
              480 : { items : 1  }, // from zero to 480 screen width 4 items
              768 : { items : 3  }, // from 480 screen widthto 768 6 items
              1025 : { items : 4   // from 768 screen width to 1024 8 items
              }
          },
    });
});

// validation for Profile iNfo starts here
    validator = $("#profile_info").validate({
        rules: {
            first_name: {
                required: true,
            },
             mobile_no: {
                digits: true,
                minlength: 10,
                maxlength: 10,
                required: true,
                
            },
            email: {
                required: true,
                email: true,
            },
            last_name: {
                required: true,
            },
            pincode : {
                required : true,
                maxlength: 6,
                digits: true,
                minlength: 6,
            },
            address_line1 : {
                required:true,
            },
            address_line2 : {
                required : true,
            },
            city_name : {
                required : true,
            },
            state_name : {
                required : true,
            }
            
        },
        messages: {
            first_name: {
                required: "This field is required",
            },
             mobile_no: {
                required: "This field is required",
            },
            last_name : {
                require: "This field is required",
            },
             email: {
                required: "This field is required",
            },
            pincode : {
                required: "This field is required",
            },
            address_line1 : {
                required: "This field is required",
            },
            address_line2 : {
                required: "This field is required",
            },
             city_name : {
                required: "This field is required",
            },
            state_name : {
                required: "This field is required",
            },
        },
    });
// validation for forgot Password ends here


/********* Showing & Hiding Password on click - starts *******/
// function myFunction() {
$(document.body).on('click','.show_password',function(){
  var info_id = $(this).data('info'); 
  var pswd_id = document.getElementById(info_id);
  if (pswd_id.type === "password") {
    pswd_id.type = "text";
  } else {
    pswd_id.type = "password";
  }
});
/********* Showing & Hiding Password on click - ends *******/


// validation for Admin Approval Status starts here
    validator = $("#admin_approval_reg").validate({
        rules: {
            regsr_no: {
                required: true,
            },
            prfile_status_id: {
                required: true,
            },
            message: {
                required: true,
            },
           
        },
        messages: {
            regsr_no: {
                required: "This field is required",
            },
            prfile_status_id: {
                required: "This field is required",
            },
            message: {
                required: "This field is required",
            },
           }
    });
});