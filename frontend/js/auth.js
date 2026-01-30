loginBtn.onclick = () => {
  if (!email.value || !password.value) {
    alert("Fill all fields");
    return;
  }

  Session.setUser({
    id: Date.now(),
    email: email.value,
    role: "user",
    coach_id: 1
  });

  window.location.href = "focus.html";
};
