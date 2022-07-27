from crypt import methods
from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "Here we again"


@app.route("/")
def index():
    if "total_gold" not in session:
        session["total_gold"] = 0
    return render_template("index.html")


@app.route("/process_gold", methods=["POST"])
def process_gold():
    print(f"entered process the value is {request.form.keys()}")
    farm = random.randint(1, 10)
    cave = random.randint(5, 10)
    house = random.randint(2, 5)
    casino = random.randint(0, 50)
    if "farm" in request.form:
        session["total_gold"] += farm
    elif "cave" in request.form:
        session["total_gold"] += cave
    elif "house" in request.form:
        session["total_gold"] += house
    elif "casino" in request.form:
        choice = random.randint(0, 10)
        if choice >= 5:
            session["total_gold"] += casino
        else:
            session["total_gold"] -= casino
    print(session["total_gold"])
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
