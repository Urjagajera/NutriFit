const express = require("express");
const fs = require("fs");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

const FILE = "./data.json";
const read = () => JSON.parse(fs.readFileSync(FILE));
const write = d => fs.writeFileSync(FILE, JSON.stringify(d, null, 2));

const today = () => new Date().toISOString().split("T")[0];

/* Get today data */
app.get("/api/today", (req, res) => {
  const data = read();
  const date = today();

  if (!data.history[date]) {
    data.history[date] = {
      calories: [],
      water: [],
      rating: null
    };
    write(data);
  }

  res.json({
    profile: data.profile,
    goals: data.goals,
    today: data.history[date]
  });
});

/* Add calories */
app.post("/api/calories", (req, res) => {
  const { value } = req.body;
  const data = read();
  data.history[today()].calories.push(value);
  write(data);
  res.json(data.history[today()]);
});

/* Add water */
app.post("/api/water", (req, res) => {
  const data = read();
  data.history[today()].water.push(250);
  write(data);
  res.json(data.history[today()]);
});

/* Save rating */
app.post("/api/rating", (req, res) => {
  const data = read();
  data.history[today()].rating = req.body.rating;
  write(data);
  res.json({ success: true });
});

app.listen(3000, () => console.log("✅ Backend running"));
