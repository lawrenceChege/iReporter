let mainNav = document.getElementById('navbar-right');
let navBarToggle = document.getElementById('navbar-toggle');

navBarToggle.addEventListener('click', function () {
  mainNav.classList.toggle('active');
});

function openPage(pageName, elmnt, color) {
  // Hide all elements with class="tabcontent" by default */
  let i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("flex-container");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  // Remove the background color of all tablinks/buttons
  tablinks = document.getElementsByClassName("button");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }

  // Show the specific tab content
  document.getElementById(pageName).style.display = "flex";

  // Add the specific color to the button used to open the tab content
  elmnt.style.backgroundColor = color;
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

function createNewFlag() {
  window.location = "createflag.html"
}
function createIntervention() {
  window.location = "createintervention.html"
}
function initMap(location) {
  // The location of Uluru
  let uluru = { location };
  // The map, centered at Uluru
  let map = new google.maps.Map(
    document.getElementById('map'), { zoom: 4, center: uluru });
  // The marker, positioned at Uluru
  let marker = new google.maps.Marker({ position: uluru, map: map });
}
// the incident modal
// let modal = document.getElementById('viewIncident');
// let btn = document.getElementById("mymodal");
// let span = document.getElementsByClassName("close")[0];
// btn.onclick = function() {
//   modal.style.display = "block";
// }
// span.onclick = function() {
//   modal.style.display = "none";
// }
// window.onclick = function(event) {
//   if (event.target == modal) {
//     modal.style.display = "none";
//   }
// }