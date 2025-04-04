from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_frozen import Freezer


app = Flask(__name__)
Bootstrap5(app)
freezer = Freezer(app)


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


@app.route("/automated-cookie-clicker")
def cookieclicker():
    return render_template("cookieclicker.html")


@app.route("/entertainment-tracker")
def entertainmenttracker():
    return render_template("entertainmenttracker.html")


@app.route("/space-evaders")
def spaceevaders():
    return render_template("spaceevaders.html")


@app.route("/snake")
def snake():
    return render_template("snake.html")


@app.route("/list-of-top-movies")
def topmovies():
    return render_template("topmovies.html")


if __name__ == "__main__":
    app.run(debug=True)
    freezer.freeze()
