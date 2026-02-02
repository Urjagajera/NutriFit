from flask import Flask, request, redirect
import user_logic
import admin_logic

app = Flask(__name__)

# ---------- USER ----------

@app.route("/register", methods=["POST"])
def register():
    user_logic.register_user(
        request.form["email"],
        request.form["password"]
    )
    return redirect("/focus.html")


@app.route("/login", methods=["POST"])
def login():
    ok = user_logic.login_user(
        request.form["email"],
        request.form["password"]
    )
    return redirect("/dashboard.html") if ok else "Invalid login"


@app.route("/save_profile", methods=["POST"])
def save_profile():
    user_logic.save_user_quiz(request.form)
    return redirect("/dashboard.html")


# ---------- ADMIN ----------

@app.route("/admin/login", methods=["POST"])
def admin_login():
    if admin_logic.admin_login(
        request.form["email"],
        request.form["password"]
    ):
        return redirect("/admin/admin_dashboard.html")
    return "Invalid admin login"


@app.route("/admin/see_users")
def see_users():
    users = admin_logic.fetch_all_users()

    rows = ""
    for _, u in users.iterrows():
        rows += f"""
        <tr>
          <td>{u.user_id}</td>
          <td>{u.email}</td>
          <td>{u.focus}</td>
          <td>{u.age}</td>
          <td>{u.gender}</td>
          <td>{u.height}</td>
          <td>{u.weight}</td>
          <td>{u.food}</td>
          <td>{u.sleep}</td>
          <td>{u.medical}</td>
        </tr>
        """

    html = open("frontend/admin/see_users.html").read()
    html = html.replace("</table>", rows + "</table>")
    return html


app.run(debug=True)
