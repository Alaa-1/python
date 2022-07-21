from flask import Flask, jsonify

app = Flask(__name__)


@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404


@app.route("/")
def hello_world():
    return "Hello Mate"


@app.route("/dojo")
def dojo():
    return "Dojo"


@app.route("/count/<int:times>")
def count(times):
    return f"{times} times"


@app.route("/hi/<string:name>")
def hi(name):
    print(type(name))
    return f"Hi {name}"


if __name__ == "__main__":
    app.run(debug=True)
