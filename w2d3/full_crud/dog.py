from mysqlconnection import connectToMySQL

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
    def get_one(cls, data):
        query = "SELECT * FROM dogs WHERE id = %(id)s;"
        results = connectToMySQL("dogs_db").query_db(query, data)
        if results:
            return cls(results[0])


    @classmethod
    def update_dog(cls, data):
        query = "UPDATE dogs SET name = %(name)s, age = %(age)s, hair_color = %(hair_color)s WHERE id = %(id)s;"
        connectToMySQL("dogs_db").query_db(query, data)


    @classmethod
    def delete_dog(cls, data):
        query = "DELETE FROM dogs WHERE id = %(id)s;"
        connectToMySQL("dogs_db").query_db(query, data)