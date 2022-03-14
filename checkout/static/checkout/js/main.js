/* jshint esversion: 6 */
// static/main.js


stripeElements();

function stripeElements() {
    stripe = Stripe('pk_test_51KP3luCfV7tzQZJ8llt1RmpeC4OJwDyoEWAQjqZ34aR5oJDUdabnEw4xqcVKNt7May8kIXdYyEBEjVraLZ1hPQQa00LFEFSrWL');

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
            displayError(event);
        });
    }
    //we'll add payment form handling here
}

function displayError(event) {

    let displayError = document.getElementById('card-errors');
    if (event.error) {
        displayError.textContent = event.error.message;
    } else {
        displayError.textContent = '';
    }
}


//we'll add payment form handling here
let paymentForm = document.getElementById('subscription-form');
if (paymentForm) {

    paymentForm.addEventListener('submit', function(evt) {
        evt.preventDefault();
        $('#submit-button').attr('disabled', true);
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);


        // create new payment method & create subscription
        createPaymentMethod({
            card
        });
    });
}

function createPaymentMethod({
    card
}) {

    // Set up payment method for recurring usage
    let billingName = '{{user.username}}';

    stripe
        .createPaymentMethod({
            type: 'card',
            card: card,
            billing_details: {
                name: billingName,
            },
        })
        .then((result) => {
            if (result.error) {
                displayError(result);
            } else {
                const paymentParams = {
                    price_id: document.getElementById("priceId").innerHTML,
                    payment_method: result.paymentMethod.id,
                };
                fetch("create-sub/", {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': '{{ csrf_token }}',
                    },
                    credentials: 'same-origin',
                    body: JSON.stringify(paymentParams),
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

                        window.location.href = 'subscribe';
                    };
                }).catch(() => {
                    displayError(result.error.message);
                    $('#payment-form').fadeToggle(100);
                    $('#loading-overlay').fadeToggle(100);

                });
            }
        });
}