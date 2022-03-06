/* jshint esversion: 6 */
// static/main.js

function planSelect(name, price, priceId, url, caption, price_only) {
    var inputs = document.getElementsByTagName('input');

    for (var i = 0; i < inputs.length; i++) {
        inputs[i].checked = false;
        if (inputs[i].name == name) {

            inputs[i].checked = true;
        }
    }
    var n = document.getElementById('name');
    var p = document.getElementById('price');
    var pid = document.getElementById('priceId');
    var ur = document.getElementById('url');
    var cap = document.getElementById('caption');
    var po = document.getElementById('price_only');
    n.value = name;
    p.value = price;
    pid.value = priceId;
    ur.value = url;
    cap.value = caption;
    po.value = price_only;

}