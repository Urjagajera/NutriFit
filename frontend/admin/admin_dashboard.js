// Admin page protection
if (!Session.isAdminLoggedIn()) {
  window.location.href = "admin_login.html";
}

// Logout
document.getElementById("admin-logout").onclick = () => {
  Session.clearAdmin();
};

// View Users
document.getElementById("btn-view-users").onclick = () => {
  alert("User list page will be added next");
};

// Upload Diet
document.getElementById("btn-upload-diet").onclick = () => {
  const userId = document.getElementById("diet-user-select").value;
  if (!userId) return alert("Select a user first");
  alert(`Diet plan upload for user ID ${userId}`);
};

// Upload Workout
document.getElementById("btn-upload-workout").onclick = () => {
  const userId = document.getElementById("workout-user-select").value;
  if (!userId) return alert("Select a user first");
  alert(`Workout plan upload for user ID ${userId}`);
};

// View Progress
document.getElementById("btn-view-progress").onclick = () => {
  alert("User progress analytics coming next");
};

// Reports
document.getElementById("btn-download-reports").onclick = () => {
  alert("Report download feature coming next");
};
