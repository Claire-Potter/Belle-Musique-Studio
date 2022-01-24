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
navBar.onclick = function (event) {
  if (!event.target.matches(".steps-button")) {
      for (i = 0; i < dropdowns.length; i++) {
      if (openDropdown.classList.contains("show")) {
        openDropdown.classList.remove("show");
      }
    }
  }
};

dropButton.addEventListener("click", dropdownMenu);

// https://getbootstrap.com/docs/5.0/components/tooltips/
// referenced and edited for
// tooltips

const tooltipTriggerList = [].slice.call(document
                                         .querySelectorAll(
                                         "[data-bs-toggle='tooltip']"));
const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
  return new bootstrap.Tooltip(tooltipTriggerEl);
});
