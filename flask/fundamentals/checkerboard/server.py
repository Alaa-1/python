from flask import Flask, render_template

app = Flask(__name__)

# http://localhost:5000 - should display 8 by 8 checkerboard
@app.route("/")
def root():
    return render_template("index.html", x=8, y=8)


# http://localhost:5000/4 - should display 8 by 4 checkerboard
@app.route("/<x>")
def eight_by_x(x, color1="#CD0000", color2="#000"):
    return render_template("custom.html", y=8, x=int(x), color1=color1, color2=color2)


# http://localhost:5000/(x)/(y) - should display x by y checkerboard
@app.route("/<x>/<y>")
def x_by_y(x, y, color1="#CD0000", color2="#000"):
    return render_template(
        "custom.html", x=int(x), y=int(y), color1=color1, color2=color2
    )


# http://localhost:5000/(x)/(y)/(color1)/(color2)
# - should display x by y checkerboard with alternating colors, color1 and color2
@app.route("/<x>/<y>/<color1>/<color2>")
def sensai_bonus(x, y, color1, color2):
    return render_template(
        "custom.html", x=int(x), y=int(y), color1=color1, color2=color2
    )


if __name__ == "__main__":
    app.run(debug=True)
