document.getElementById("admin-login-form").onsubmit = (e) => {
  e.preventDefault();

  const email = document.getElementById("admin-email").value;
  const password = document.getElementById("admin-password").value;

  // MOCK ADMIN AUTH (replace later with PHP)
  if (email === "ruchigajera33@gmail.com" && password === "ruchi,18.") {
    Session.setAdmin({
      email,
      role: "admin"
    });

    window.location.href = "admin_dashboard.html";
  } else {
    alert("Invalid admin credentials");
  }
};
