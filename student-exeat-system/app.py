from flask import Flask, render_template, request, redirect, session, url_for
).fetchone()


if user:
session["user_id"] = user["id"]
session["role"] = user["role"]
return redirect("/dashboard")
return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
if request.method == "POST":
name = request.form["name"]
matric = request.form["matric"]
password = request.form["password"]


db = get_db()
db.execute(
"INSERT INTO users (name, matric_no, password, role) VALUES (?, ?, ?, 'student')",
(name, matric, password)
)
db.commit()
return redirect("/")
return render_template("register.html")


@app.route("/dashboard")
def dashboard():
db = get_db()
exeats = db.execute(
"SELECT * FROM exeats WHERE user_id=?",
(session.get("user_id"),)
).fetchall()
return render_template("dashboard.html", exeats=exeats)


@app.route("/apply", methods=["GET", "POST"])
def apply():
if request.method == "POST":
reason = request.form["reason"]
dep = request.form["departure"]
ret = request.form["return"]


db = get_db()
db.execute(
"INSERT INTO exeats (user_id, reason, departure_date, return_date, status, created_at) VALUES (?, ?, ?, ?, 'Pending', ?)",
(session.get("user_id"), reason, dep, ret, datetime.now())
)
db.commit()
return redirect("/dashboard")
return render_template("apply_exeat.html")


@app.route("/admin")
def admin():
db = get_db()
exeats = db.execute(
"SELECT exeats.*, users.name FROM exeats JOIN users ON exeats.user_id = users.id"
).fetchall()
return render_template("admin.html", exeats=exeats)


@app.route("/approve/<int:id>")
def approve(id):
db = get_db()
db.execute("UPDATE exeats SET status='Approved' WHERE id=?", (id,))
db.commit()
return redirect("/admin")


@app.route("/reject/<int:id>")
def reject(id):
db = get_db()
db.execute("UPDATE exeats SET status='Rejected' WHERE id=?", (id,))
db.commit()
return redirect("/admin")


if __name__ == "__main__":
app.run(debug=True)