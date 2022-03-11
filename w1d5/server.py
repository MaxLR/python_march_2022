from flask import Flask, render_template, request, redirect, session #import flask & render template
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_record", methods = ["POST"])
def create_record():
    if "pet_name" in request.form and request.form["pet_name"] != "":
        if "favorite_food" in request.form and request.form["favorite_food"] != "":
            print("Got the post data")
            print(request.form)
            pet_name = request.form["pet_name"]
            favorite_food = request.form["favorite_food"]
            return render_template("success.html", pet_name = pet_name, favorite_food = favorite_food)
    return redirect("/")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/login", methods = ["POST"])
def login():
    session["username"] = request.form["username"]
    session["email"] = request.form["email"]
    session["hidden_input"] = request.form["hidden_input"]
    print(session)
    return render_template("show.html")


@app.route("/clear_session")
def clear_session():
    session.clear()
    return redirect("/dashboard")



if __name__ == "__main__":
    app.run(debug=True)