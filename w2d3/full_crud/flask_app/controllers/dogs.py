from flask import Flask, render_template, redirect, request  # Import Flask to allow us to create our app
from flask_app import app
from flask_app.models.dog import Dog


# DISPLAY ROUTES -----------------------

@app.route("/")
def index():
    dogs = Dog.get_all_dogs()
    return render_template("index.html", all_dogs = dogs)

@app.route("/dogs/new")
def new_dog():
    return render_template("add_dog.html")

@app.route("/dogs/<int:id>")
def show_dog(id):
    data = { "id": id }
    dog = Dog.get_one_with_collars(data)
    return render_template("show_dog.html", dog = dog)


@app.route("/dogs/edit/<int:id>")
def edit_dog(id):
    dog = Dog.get_one({ "id": id })
    return render_template("edit_dog.html", dog = dog)


# ACTION ROUTES -----------------------

@app.route("/dogs/create", methods = ["POST"])
def create_dog():
    if Dog.validate_dog(request.form):
        Dog.create_dog(request.form)
        return redirect('/')
    return redirect("/dogs/new")

@app.route("/dogs/update", methods = ["POST"])
def update_dog():
    if Dog.validate_dog(request.form):
        Dog.update_dog(request.form)
        return redirect('/')
    dog_id = request.form["id"]
    return redirect(f"/dogs/edit/{dog_id}")


@app.route("/dogs/<int:id>/delete")
def delete_dog(id):
    Dog.delete_dog({ "id": id })
    return redirect('/')