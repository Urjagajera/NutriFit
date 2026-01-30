const MockAPI = (() => {

  let store = {
    goals: { calories: 2000, water: 3000 },
    today: {
      date: new Date().toDateString(),
      calories: [],
      water: [],
      rating: null
    }
  };

  return {

    getToday() {
      return Promise.resolve({
        goals: store.goals,
        today: store.today
      });
    },

    addCalories(value) {
      store.today.calories.push(value);
      return Promise.resolve(store.today);
    },

    addWater() {
      store.today.water.push(250);
      return Promise.resolve(store.today);
    },

    addRating(rating) {
      store.today.rating = rating;
      return Promise.resolve(true);
    }

  };
})();
