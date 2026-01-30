// Page protection
if (!Session.isLoggedIn()) {
  window.location.href = "index.html";
}

// Logout
document.getElementById("nav-logout").onclick = () => {
  Session.clear();
};

// Simulated backend (for testing without server)
let goals = { calories: 2000, water: 3000 };
let today = { calories: [], water: [], rating: null };

const calBar = document.getElementById("calorieProgress");
const waterBar = document.getElementById("waterProgress");
const table = document.getElementById("dailyTable");
const badge = document.getElementById("statusBadge");

const totalCalories = document.getElementById("totalCalories");
const totalWater = document.getElementById("totalWater");
const addCalories = document.getElementById("addCalories");

// Load user data from session
const user = Session.getUser();
if (user) {
  document.getElementById("profile-name").innerText =
    user.email.split("@")[0];

  document.getElementById("profile-focus").innerText =
    user.focus || "Not Set";

  document.getElementById("detail-email").innerText = user.email;
  document.getElementById("detail-goal").innerText = user.focus || "Not Set";

  if (user.profile) {
    document.getElementById("detail-age").innerText = user.profile.age;
    document.getElementById("detail-gender").innerText = user.profile.gender;
    document.getElementById("detail-height").innerText = user.profile.height;
    document.getElementById("detail-weight").innerText = user.profile.weight;
    document.getElementById("detail-food").innerText = user.profile.food_habit;
    document.getElementById("detail-allergies").innerText = user.profile.allergies;
    document.getElementById("detail-sleep").innerText = user.profile.sleep_hours;
    document.getElementById("detail-medical").innerText = user.profile.medical_condition;
    document.getElementById("detail-commitment").innerText = user.profile.commitment_level;
    document.getElementById("detail-bmi").innerText = user.profile.bmi;
    document.getElementById("detail-bmr").innerText = user.profile.bmr;
  }
}

function updateUI() {
  const calSum = today.calories.reduce((a, b) => a + b, 0);
  const waterSum = today.water.reduce((a, b) => a + b, 0);

  calBar.style.width = (calSum / goals.calories * 100) + "%";
  waterBar.style.width = (waterSum / goals.water * 100) + "%";

  let calPercent = calSum / goals.calories;
  badge.className =
    "badge animate " +
    (calPercent > 1 ? "red" : calPercent > 0.7 ? "green" : "yellow");

  badge.innerText =
    calPercent > 1 ? "Over Limit" :
    calPercent > 0.7 ? "On Track" :
    "Needs Attention";

  table.innerHTML = "<tr><th>Type</th><th>Value</th></tr>";
  today.calories.forEach(c =>
    table.innerHTML += `<tr><td>Calories</td><td>${c}</td></tr>`
  );
  today.water.forEach(w =>
    table.innerHTML += `<tr><td>Water</td><td>${w} ml</td></tr>`
  );

  document.getElementById("todayRating").innerText =
    today.rating ? today.rating + " ★" : "Not Rated";
}

// EVENTS
document.getElementById("addCaloriesBtn").onclick = () => {
  let val = parseInt(addCalories.value);
  if (!val) return alert("Enter calories");
  today.calories.push(val);
  addCalories.value = "";
  updateUI();
};

document.getElementById("addWaterBtn").onclick = () => {
  today.water.push(250);
  updateUI();
};

document.getElementById("changeCaloriesBtn").onclick = () => {
  totalCalories.disabled = false;
  totalCalories.focus();
};

totalCalories.onblur = () => {
  totalCalories.disabled = true;
  goals.calories = parseInt(totalCalories.value);
  updateUI();
};

document.getElementById("changeWaterBtn").onclick = () => {
  totalWater.disabled = false;
  totalWater.focus();
};

totalWater.onblur = () => {
  totalWater.disabled = true;
  goals.water = parseInt(totalWater.value);
  updateUI();
};

document.getElementById("submitRatingBtn").onclick = () => {
  const r = document.querySelector('input[name="rating"]:checked')?.value;
  if (!r) return alert("Select rating");
  today.rating = r;
  updateUI();
};

updateUI();
