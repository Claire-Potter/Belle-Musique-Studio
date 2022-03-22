/* jshint esversion: 6 */
// static/main.js
$('#submit-button').attr('disabled', true);
bagValue();

function bagValue() {
    var lessonTotal = document.getElementById('lesson-bag-total').innerHTML;
    console.log(lessonTotal)
    Number(lessonTotal);

    if (lessonTotal == 0.00)
        $('.select-buttons').attr('disabled', false);
    else
        $('.select-buttons').attr('disabled', true);

}

function planSelect(name, price, priceId, url, caption, price_only, dj_stripe_id) {

    var n = document.getElementById('name');
    var p = document.getElementById('price');
    var pid = document.getElementById('priceId');
    var ur = document.getElementById('url');
    var cap = document.getElementById('caption');
    var po = document.getElementById('price_only');
    var dj = document.getElementById('dj_stripe');
    n.value = name;
    p.value = price;
    pid.value = priceId;
    ur.value = url;
    cap.value = caption;
    po.value = price_only;
    dj.value = dj_stripe_id;
    $('#submit-button').attr('disabled', false);

}