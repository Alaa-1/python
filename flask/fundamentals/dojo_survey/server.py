from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "Here we go again"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/info", methods=["POST"])
def fetch_info():
    session["username"] = request.form["username"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comment"] = request.form["comment"]
    return redirect("/results")


@app.route("/results")
def result():
    return render_template("results.html")


@app.route("/go_home")
def redirect_home():
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
