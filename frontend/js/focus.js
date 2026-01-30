// Protect page (no direct access)
if (!Session.isLoggedIn()) {
  window.location.href = "index.html";
}

const focusForm = document.getElementById("focusForm");
const focusSelect = document.getElementById("focusSelect");

focusForm.onsubmit = (e) => {
  e.preventDefault();

  if (!focusSelect.value) {
    alert("Please select a focus");
    return;
  }

  // Get current user session
  const user = Session.getUser();

  // Save focus (acts like backend save)
  user.focus = focusSelect.value;
  user.focus_selected_at = new Date().toISOString();

  Session.setUser(user);

  // Move to next step
  window.location.href = "quiz.html";
};
