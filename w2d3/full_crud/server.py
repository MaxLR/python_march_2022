from sqlite3 import connect
from flask import Flask, render_template, redirect, request  # Import Flask to allow us to create our app
from mysqlconnection import connectToMySQL
from dog import Dog

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


# DISPLAY ROUTES -----------------------

@app.route("/")
def index():
    mysql = connectToMySQL("dogs_db") #how we connect to a database
    dogs = mysql.query_db("SELECT * FROM dogs;")
    return render_template("index.html", all_dogs = dogs)

@app.route("/dogs/new")
def new_dog():
    return render_template("add_dog.html")

@app.route("/dogs/<int:id>")
def show_dog(id):
    data = { "id": id }
    dog = Dog.get_one(data)
    return render_template("show_dog.html", dog = dog)


@app.route("/dogs/edit/<int:id>")
def edit_dog(id):
    dog = Dog.get_one({ "id": id })
    return render_template("edit_dog.html", dog = dog)


# ACTION ROUTES -----------------------

@app.route("/dogs/create", methods = ["POST"])
def create_dog():
    Dog.create_dog(request.form)
    return redirect('/')


@app.route("/dogs/update", methods = ["POST"])
def update_dog():
    Dog.update_dog(request.form)
    return redirect('/')


@app.route("/dogs/<int:id>/delete")
def delete_dog(id):
    Dog.delete_dog({ "id": id })
    return redirect('/')


# Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

