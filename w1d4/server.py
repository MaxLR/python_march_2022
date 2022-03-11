from flask import Flask, render_template #import Flask and use create our app
app = Flask(__name__)


#Creating our first route
@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/success")
def success():
    return "Success!!!! We did it!"


#Passing in variables through the URL
@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}"


#Specifying data types that come through URL variables
@app.route("/users/<string:username>/<int:id>")
def users(username, id):
    return f"Username: {username}, ID: {id}"


#RENDERING OUR FIRST HTML PAGE W/ FLASK!!!
@app.route("/index")
def index():
    #pass in the name of the html file & any variables that we plan to use on that page
    return render_template("index.html", my_string="Hello", times = 5)


@app.route("/lists")
def lists():
    student_list = [
        {"name": "max", "id": "7"},
        {"name": "christian", "id": "1"},
        {"name": "amanda", "id": "3"},
        {"name": "hiago", "id": "21"}
    ]
    return render_template("list.html", students = student_list, my_nums = [1, 3 ,6, 3, 19])


if __name__ == "__main__":
    app.run(debug=True)