/* jshint esversion: 6 */
/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/


// Handle form submit
var form = document.getElementById('subscription-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'save_info': saveInfo,
    };

    var url = 'cache_checkout_data_lesson/';

    $.post(url, postData).done(function() {
        {
            form.submit();
        }
    });
})