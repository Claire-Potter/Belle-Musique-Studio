/* jshint esversion: 6 */
// static/main.js

console.log("Sanity check!");
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_stripe_secret_key').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);

document.getElementById("submit").disabled = true;

stripeElements();

function stripeElements() {

    if (document.getElementById('card-element')) {
        let elements = stripe.elements();

        // Card Element styles
        let style = {
            base: {
                color: "#32325d",
                fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
                fontSmoothing: "antialiased",
                fontSize: "16px",
                "::placeholder": {
                    color: "#aab7c4"
                }
            },
            invalid: {
                color: "#fa755a",
                iconColor: "#fa755a"
            }
        };


        card = elements.create('card', {
            style: style
        });

        card.mount('#card-element');

        card.on('focus', function() {
            let el = document.getElementById('card-errors');
            el.classList.add('focused');
        });

        card.on('blur', function() {
            let el = document.getElementById('card-errors');
            el.classList.remove('focused');
        });

        card.on('change', function(event) {
            var errorDiv = document.getElementById('card-errors');
            if (event.error) {
                var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
                $(errorDiv).html(html);
            } else {
                errorDiv.textContent = '';
            }
        });
    }
    //we'll add payment form handling here


}

//we'll add payment form handling here
let paymentForm = document.getElementById('subscription-form');
if (paymentForm) {

    paymentForm.addEventListener('submit', function(ev) {
        ev.preventDefault();
        card.update({
            'disabled': true
        });
        $('#submit').attr('disabled', true);
        $('#subscription-form').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);

        // create new payment method & create subscription
        createPaymentMethod({
            card
        });
    });
}

var saveInfo = Boolean($('#id-save-info').attr('checked'));
// From using {% csrf_token %} in the form
var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
var postData = {
    'csrfmiddlewaretoken': csrfToken,
    'client_secret': clientSecret,
    'save_info': saveInfo,
};

var url = '/checkout_lesson/cache_checkout_data_lesson/';
document.getElementById("submit").disabled = false;

function createPaymentMethod({
    card
}) {
    let billingName = '{{user.username}}';
    stripe
        .createPaymentMethod({
            type: 'card',
            card: card,
            billing_details: {
                name: billingName,
            },
        }).then((result) => {
            if (result.error) {
                displayError(result);
            } else {
                const paymentParams = {
                    price_id: document.getElementById("priceId").innerHTML,
                    payment_method: result.paymentMethod.id,
                };
                fetch('/checkout_lesson/cache_checkout_data_lesson/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': csrfToken,
                    },
                    credentials: 'same-origin',
                    body: JSON.stringify(paymentParams),
                    'save_info': saveInfo,
                }).then((response) => {
                    return response.json();
                }).then((result) => {
                    if (result.error) {
                        // The card had an error when trying to attach it to a customer
                        throw result;
                    }
                    return result;
                }).then((result) => {
                    if (result && result.status === 'active') {

                        window.location.href = 'complete/';
                    };
                }).catch(() => {
                    displayError(result.error.message);

                });
            }
        });
}