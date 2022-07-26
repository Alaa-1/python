from crypt import methods
from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "keep it secret"


@app.route("/")
def index():
    if "visited" in session:
        session["visited"] += 1
    else:
        session["visited"] = 1
        session["count"] = 0

    return render_template("index.html")


@app.route("/destroy_session")
def destroy_session():
    if "count" in session:
        session.clear()
    return redirect("/")


@app.route("/increment_2", methods=["POST"])
def increment_2():
    if "count" in session:
        print("yes it is")
        # refresh root already increments by 1, increment_2() redirects to root
        session["count"] += 2
        print(f"Icrement by 2")
    return redirect("/")


@app.route("/reset", methods=["POST"])
def reset():
    if "count" in session:
        session.clear()
    return redirect("/")


@app.route("/manual_increment", methods=["POST"])
def manual_increment():
    if "count" in session and request.form["count_num"]:
        print(f"******{request.form['count_num']}")
        session["count"] += int(request.form["count_num"])
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
