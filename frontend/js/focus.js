focusBtn.onclick = async () => {
  await fetch("backend/api/save_focus.php", {
    method: "POST",
    body: JSON.stringify({
      user_id: localStorage.getItem("user_id"),
      focus: focusSelect.value
    })
  });
  window.location = "quiz.html";
};
