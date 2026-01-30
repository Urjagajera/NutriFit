// Safety check (optional but good)
if (Session.isLoggedIn()) {
  window.location.href = "dashboard.html";
}

const registerForm = document.getElementById("registerForm");
const regEmail = document.getElementById("regEmail");
const regPassword = document.getElementById("regPassword");
const regConfirmPassword = document.getElementById("regConfirmPassword");

registerForm.onsubmit = (e) => {
  e.preventDefault();

  // Basic validation
  if (!regEmail.value || !regPassword.value || !regConfirmPassword.value) {
    alert("Please fill all fields");
    return;
  }

  if (regPassword.value !== regConfirmPassword.value) {
    alert("Passwords do not match");
    return;
  }

  // MOCK REGISTER (acts like backend)
  const newUser = {
    id: Date.now(),                 // later → DB auto ID
    email: regEmail.value,
    role: "user",
    coach_id: 1,                    // one coach → many users
    created_at: new Date().toISOString()
  };

  // Store session
  Session.setUser(newUser);

  // Redirect to next step
  window.location.href = "focus.html";
};
