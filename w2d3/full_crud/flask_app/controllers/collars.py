from flask import Flask, render_template, redirect, request
from flask_app import app
from flask_app.models.collar import Collar


# DISPLAY ROUTES --------------------------------
@app.route("/collars")
def all_collars():
    collars = Collar.get_all()
    return render_template("collars.html", collars = collars)





# ACTION ROUTES -----------------------------
@app.route("/collars/create", methods = ["POST"])
def create_collar():
    Collar.create(request.form)
    dog_id = request.form["dog_id"]
    return redirect(f"/dogs/{dog_id}")

