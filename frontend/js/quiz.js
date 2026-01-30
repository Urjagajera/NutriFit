// Page protection
if (!Session.isLoggedIn()) {
  window.location.href = "index.html";
}

const quizForm = document.getElementById("quizForm");

quizForm.onsubmit = (e) => {
  e.preventDefault();

  // Basic validation
  if (
    !age.value || !gender.value || !height.value ||
    !weight.value || !foodHabit.value ||
    !sleepHours.value || !medical.value || !commitment.value
  ) {
    alert("Please fill all required fields");
    return;
  }

  const user = Session.getUser();

  // Store quiz data (acts like backend save)
  user.profile = {
    age: Number(age.value),
    gender: gender.value,
    height: Number(height.value),
    weight: Number(weight.value),
    food_habit: foodHabit.value,
    allergies: allergies.value || "None",
    sleep_hours: Number(sleepHours.value),
    medical_condition: medical.value,
    commitment_level: commitment.value,
    submitted_at: new Date().toISOString()
  };

  // BMI calculation (report ready)
  user.profile.bmi = (
    user.profile.weight /
    ((user.profile.height / 100) ** 2)
  ).toFixed(2);

  // BMR calculation (future AI use)
  if (user.profile.gender === "male") {
    user.profile.bmr =
      88.36 +
      (13.4 * user.profile.weight) +
      (4.8 * user.profile.height) -
      (5.7 * user.profile.age);
  } else {
    user.profile.bmr =
      447.6 +
      (9.2 * user.profile.weight) +
      (3.1 * user.profile.height) -
      (4.3 * user.profile.age);
  }

  user.profile.bmr = Math.round(user.profile.bmr);

  // Save session
  Session.setUser(user);

  // Next page
  window.location.href = "dashboard.html";
};
