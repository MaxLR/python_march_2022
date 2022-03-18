from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import collar

class Dog:
    def __init__(self, data):
        #data is a dictionary
        self.id = data["id"]
        self.name = data["name"]
        self.age = data["age"]
        self.hair_color = data["hair_color"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create_dog(cls, data):
        mysql = connectToMySQL("dogs_db")

        query = "INSERT INTO dogs (name, age, hair_color) VALUES (%(name)s, %(age)s, %(hair_color)s);"

        return mysql.query_db(query, data) #will return the ID of the dog created


    @classmethod
    def get_all_dogs(cls):
        mysql = connectToMySQL("dogs_db") #how we connect to a database
        results = mysql.query_db("SELECT * FROM dogs;")
        all_dogs = []
        if results:
            for row in results:
                all_dogs.append(cls(row))
            return all_dogs


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dogs WHERE id = %(id)s;"
        results = connectToMySQL("dogs_db").query_db(query, data)
        if results:
            return cls(results[0])


    @classmethod
    def get_one_with_collars(cls, data):
        query = "SELECT * FROM dogs LEFT JOIN collars ON dogs.id = collars.dog_id WHERE dogs.id = %(id)s;"
        results = connectToMySQL("dogs_db").query_db(query, data)
        if results:
            dog = cls(results[0])
            if results[0]["collars.id"]:
                dog.collars = []
                for row in results:
                    data = {
                        #specifying collars, because our table has 2 fields called ID, one for collars, one for dogs
                        "id": row["collars.id"], 
                        "color": row["color"],
                        "dog_id": row["dog_id"],
                        "created_at": row["collars.created_at"],
                        "updated_at": row["collars.updated_at"]
                    }
                    temp_collar = collar.Collar(data)
                    dog.collars.append(temp_collar)
            return dog

    @classmethod
    def update_dog(cls, data):
        query = "UPDATE dogs SET name = %(name)s, age = %(age)s, hair_color = %(hair_color)s WHERE id = %(id)s;"
        connectToMySQL("dogs_db").query_db(query, data)


    @classmethod
    def delete_dog(cls, data):
        query = "DELETE FROM dogs WHERE id = %(id)s;"
        connectToMySQL("dogs_db").query_db(query, data)


    @staticmethod
    def validate_dog(data):
        is_valid = True

        if len(data["name"]) <= 1:
            is_valid = False
            flash("A new dog's name must be at least 2 characters long.")
        if len(data["age"]) < 1:
            is_valid = False
            flash("Dogs have to have an age")
        elif data["age"].isnumeric():
            if int(data["age"]) < 0:
                is_valid = False
                flash("Dogs can't be younger than 0!")
        else:
            is_valid = False
            flash("Please enter an actual number")
        if len(data["hair_color"]) <= 1:
            is_valid = False
            flash("Please enter a hair color with at least 2 characters!")

        return is_valid