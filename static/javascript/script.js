/* jshint esversion: 6 */
// static/script.js
/*jslint browser:true */

// Code from 'Boutique Ado' to return user to the top of the screen

$('.btt-link').click(function(e) {
    window.scrollTo(0, 0);
});

$('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if (selectedVal != "reset") {
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
});

// Create constants for html input.
const dropButton = document.getElementById("dropdown-menu-link");
const dropDown = document.getElementById("my-dropdown");
const dropdowns = document.getElementsByClassName("dropdown-menu");
const navBar = document.getElementsByClassName("navbar");
var i;
const openDropdown = dropdowns[i];

//https://www.w3schools.com/bootstrap/bootstrap_ref_js_dropdown.asp
// referenced and edited for dropdownMenu

/**
 * @function dropdownMenu When the user clicks on the button,
 * toggle between hiding and showing the dropdown content.
 */

function dropdownMenu() {
    dropDown.classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
navBar.onclick = function(event) {
    if (!event.target.matches(".steps-button")) {
        for (i = 0; i < dropdowns.length; i++) {
            if (openDropdown.classList.contains("show")) {
                openDropdown.classList.remove("show");
            }
        }
    }
};

dropButton.addEventListener("click", dropdownMenu);