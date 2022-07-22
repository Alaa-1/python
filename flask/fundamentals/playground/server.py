from distutils.log import debug
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/play")
def level_1():
    return render_template("level_1.html")


@app.route("/play/<times>")
def level_2(times):
    return render_template("level_2.html", times=int(times))


@app.route("/play/<times>/<color>")
def level_3(times, color):
    return render_template("level_3.html", times=int(times), color=color)


if __name__ == "__main__":
    app.run(debug=True)
