/* jshint esversion: 6 */
// static/submit_overlay.js
/* Javascript code from Code Institute 'Boutique Ado'
    project and customised for site purpose */

let paymentForm = document.getElementById('subscription-form');
if (paymentForm) {

    paymentForm.addEventListener('submit', function(evt) {
        evt.preventDefault();
        $('#submit-button').attr('disabled', true);
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);
    });
}