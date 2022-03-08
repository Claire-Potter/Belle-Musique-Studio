/* jshint esversion: 6 */
/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);


// Handle form submit
var form = document.getElementById('subscription-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();

    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data_lesson/';

    $.post(url, postData).done(function() {

            form.submit();
        }

    );
});