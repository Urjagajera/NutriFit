document.querySelector("form").onsubmit = async (e) => {
  e.preventDefault();

  const payload = {
    user_id: localStorage.getItem("user_id"),
    age: age.value,
    gender: gender.value,
    height: height.value,
    weight: weight.value,
    food: foodHabit.value,
    sleep: sleepHours.value
  };

  await fetch("backend/api/save_quiz.php", {
    method: "POST",
    body: JSON.stringify(payload)
  });

  window.location = "dashboard.html";
};
