from crypt import methods
from flask import Flask, render_template, session, redirect, request, url_for
import random

app = Flask(__name__)
app.secret_key = "Here we go again"


@app.route("/")
def index():
    random_num = random.randint(1, 100)
    session["random"] = random_num
    session["attempt"] = 0

    return render_template("index.html")


@app.route("/guess", methods=["POST"])
def guess():
    answer = ""

    print(f"The random number is: {session['random']}")
    if request.form["guessed_num"]:
        if int(request.form["guessed_num"]) > session["random"]:
            session["attempt"] += 1

            answer = "Too high!"

        elif int(request.form["guessed_num"]) < session["random"]:
            session["attempt"] += 1

            answer = "Too low"

        else:
            answer = f"{session['random']} was the right number!"
            session.clear()
    return render_template("/index.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=True)
