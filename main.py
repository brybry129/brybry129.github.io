from flask import Flask, render_template
from flask_bootstrap import Bootstrap5


app = Flask(__name__)
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/virtual-forge")
def virtualforge():
    return render_template("virtualforge.html")


@app.route("/shore-buddies")
def shorebuddies():
    return render_template("shorebuddies.html")


@app.route("/rick-savior")
def ricksavior():
    return render_template("ricksavior.html")


if __name__ == "__main__":
    app.run(debug=True)
