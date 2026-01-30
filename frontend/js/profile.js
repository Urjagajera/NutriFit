const API = "http://localhost:3000/api";

const calBar = document.getElementById("calorieProgress");
const waterBar = document.getElementById("waterProgress");
const table = document.getElementById("dailyTable");
const badge = document.getElementById("statusBadge");

let goals, today;

/* LOAD TODAY */
fetch(`${API}/today`)
  .then(r => r.json())
  .then(d => {
    goals = d.goals;
    today = d.today;
    updateUI();
  });

/* ADD CALORIES */
addCaloriesBtn.onclick = () => {
  const val = Number(addCalories.value);
  if (!val) return;

  fetch(`${API}/calories`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ value: val })
  })
  .then(r => r.json())
  .then(t => {
    today = t;
    updateUI();
  });

  addCalories.value = "";
};

/* ADD WATER */
addWaterBtn.onclick = () => {
  fetch(`${API}/water`, { method: "POST" })
    .then(r => r.json())
    .then(t => {
      today = t;
      updateUI();
    });
};

/* RATING */
submitRatingBtn.onclick = () => {
  const r = document.querySelector('input[name="rating"]:checked')?.value;
  if (!r) return alert("Rate your day");

  fetch(`${API}/rating`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ rating: r })
  });

  document.getElementById("todayRating").innerText = r + " ★";
};

/* UPDATE EVERYTHING */
function updateUI() {
  const calSum = today.calories.reduce((a,b)=>a+b,0);
  const waterSum = today.water.reduce((a,b)=>a+b,0);

  calBar.style.width = (calSum / goals.calories * 100) + "%";
  waterBar.style.width = (waterSum / goals.water * 100) + "%";

  badge.className = "badge animate " +
    (calSum > goals.calories ? "red" :
     calSum > goals.calories * 0.7 ? "green" : "yellow");

  renderTable();
}

/* TABLE */
function renderTable() {
  table.innerHTML = `
    <tr><th>Type</th><th>Value</th></tr>
    ${today.calories.map(c => `<tr><td>Calories</td><td>${c}</td></tr>`).join("")}
    ${today.water.map(w => `<tr><td>Water</td><td>${w} ml</td></tr>`).join("")}
  `;
}
