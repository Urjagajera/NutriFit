document.getElementById("loginBtn").onclick = async () => {
  const email = email.value;
  const password = password.value;

  const res = await fetch("backend/api/login.php", {
    method: "POST",
    body: JSON.stringify({ email, password })
  });
  const data = await res.json();

  if (data.status === "success") {
    localStorage.setItem("user_id", data.user_id);
    window.location = "dashboard.html";
  } else {
    alert("Invalid login");
  }
};
