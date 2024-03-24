/*===== SHOW NAVBAR  =====*/
const showNavbar = (toggleId, navId, bodyId, headerId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId),
    bodypd = document.getElementById(bodyId),
    headerpd = document.getElementById(headerId)

    // Validate that all variables exist
    if(toggle && nav && bodypd && headerpd){
        toggle.addEventListener('click', ()=>{
            // show navbar
            nav.classList.toggle('show')
            // change icon
            toggle.classList.toggle('bx-x')
            // add padding to body
            bodypd.classList.toggle('body-pd')
            // add padding to header
            headerpd.classList.toggle('body-pd')
        })
    }
}

showNavbar('header-toggle','nav-bar','body-pd','header')

/*===== LINK ACTIVE  =====*/
const linkColor = document.querySelectorAll('.nav__link')

function colorLink(){
    if(linkColor){
        linkColor.forEach(l=> l.classList.remove('active'))
        this.classList.add('active')
    }
}
linkColor.forEach(l=> l.addEventListener('click', colorLink))

//function load_app(appName) {
//  const appContainer = document.getElementById("app-container");
//  appContainer.innerHTML = "";  // Clear any previous content
//
//  if (appName === "student_performance") {
//    appContainer.innerHTML = "{% plotly_app name='student_performance' ratio=0.70 %}";
//  } else if (appName === "student_register") {
//    // Load content for Course Registration app (replace with your actual logic)
//    appContainer.innerHTML = "{% plotly_app name='student_register' ratio=0.70 %}";
//  } else {
//    console.error("Invalid app name:", appName);
//  }
//
//}
//
//// Call the load_app function when buttons are clicked
//
//// Get references to the buttons
//const trackPerformanceBtn = document.getElementById("track-performance-btn");
//const courseRegistrationBtn = document.getElementById("course-registration-btn");
//
// Add event listeners to the buttons
//trackPerformanceBtn.addEventListener("click", () => load_app("student_performance"));
//courseRegistrationBtn.addEventListener("click", () => load_app("student_register"));

// Get references to buttons
const trackPerformanceBtn = document.getElementById("track-performance-btn");
const courseRegistrationBtn = document.getElementById("course-registration-btn");
const appContainer = document.getElementById("app-container");
// Function to load app and update URL
function load_app(appName) {
  appContainer.innerHTML = "";  // Clear any previous content

  if (appName === "student_performance") {
    appContainer.innerHTML = "{% plotly_app name='student_performance' ratio=0.70 %}";
  } else if (appName === "student_register") {
    // Load content for Course Registration app (replace with your actual logic)
    appContainer.innerHTML = "{% plotly_app name='student_register' ratio=0.70 %}";
  } else {
    console.error("Invalid app name:", appName);
  }
}

// Add event listeners to buttons
//trackPerformanceBtn.addEventListener("click", ()=> load_app("student_performance"))
//  load_app(this.appName);
//});
//courseRegistrationBtn.addEventListener("click", function() {
//  load_app(this.appName);
//});

// Hide the scrollbar for the Dash app container
document.addEventListener('DOMContentLoaded', function() {
  var dashAppContainer = document.getElementsByClassName('dash-app-container')[0];
  dashAppContainer.style.overflow = 'hidden';
});

function changeActiveLinkColor(clickedElement) {
  // Find the currently active link (if any)
  const currentActiveLink = document.querySelector('.nav__link.active');

  // If there's a currently active link:
  if (currentActiveLink) {
    // Remove active class only if it's not the clicked link
    if (currentActiveLink !== clickedElement) {
      currentActiveLink.classList.remove('active');
    }
  } else {
    // No active link initially, so add active class to clicked link
    clickedElement.classList.add('active');
  }
}
