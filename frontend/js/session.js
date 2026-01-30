const Session = {
  setUser(user) {
    sessionStorage.setItem("nutrifit_user", JSON.stringify(user));
  },
  getUser() {
    return JSON.parse(sessionStorage.getItem("nutrifit_user"));
  },
  clear() {
    sessionStorage.clear();
    window.location.href = "index.html";
  },
  isLoggedIn() {
    return !!sessionStorage.getItem("nutrifit_user");
  }
};
