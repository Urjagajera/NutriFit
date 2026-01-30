const Session = {
    setAdmin(admin) {
    sessionStorage.setItem("admin", JSON.stringify(admin));
  },
  isAdminLoggedIn() {
    return !!sessionStorage.getItem("admin");
  },
  clearAdmin() {
    sessionStorage.removeItem("admin");
    window.location.href = "admin_login.html";
  },
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
