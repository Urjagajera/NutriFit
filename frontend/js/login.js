// If already logged in, skip login
if (Session.isLoggedIn()) {
  window.location.href = "dashboard.html";
}

const loginForm = document.getElementById("loginForm");
const loginEmail = document.getElementById("loginEmail");
const loginPassword = document.getElementById("loginPassword");

loginForm.onsubmit = (e) => {
  e.preventDefault();

  if (!loginEmail.value || !loginPassword.value) {
    alert("Please enter email and password");
    return;
  }

  // MOCK LOGIN (acts like backend auth)
  const user = {
    id: Date.now(),                 // later → DB user_id
    email: loginEmail.value,
    role: "user",
    coach_id: 1,                    // one coach → many users
    login_time: new Date().toISOString()
  };

  // Store session
  Session.setUser(user);

  // Redirect to next step
  window.location.href = "dashboard.html";
};
