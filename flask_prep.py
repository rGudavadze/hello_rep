from flask import Flask, render_template, request, redirect

app = Flask(__name__)

REGISTRANTS = {}

SPORTS = [
    "Dodgeball",
    "Football",
    "Soccer",
    "Valleyball",
    "Frisbee",
]

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message="Missing Name")
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message="Missing Sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid Sport")

    REGISTRANTS[name] = sport

    return redirect("/registrants")

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)



if __name__ == "__main__":
    app.run(debug=True)