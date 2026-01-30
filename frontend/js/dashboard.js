// Page protection
if (!Session.isLoggedIn()) {
  window.location.href = "index.html";
}

const user = Session.getUser();

/* NAVBAR */
document.getElementById("navProfile").onclick = () => {
  window.location.href = "profile.html";
};

document.getElementById("navLogout").onclick = () => {
  Session.clear();
};

/* DASHBOARD BUTTONS */
document.getElementById("btnProfile").onclick = () => {
  window.location.href = "profile.html";
};

document.getElementById("btnDiet").onclick = () => {
  alert("Diet plan module will be added next");
};

document.getElementById("btnWorkout").onclick = () => {
  alert("Workout plan module will be added next");
};

document.getElementById("btnReports").onclick = () => {
  alert("Reports & analytics coming soon");
};

/* COACH MAPPING (mock) */
if (user.coach_id === 1) {
  document.getElementById("coachName").innerText = "Coach Ruchi Gajera";
}
