from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dog

class Collar:
    def __init__(self, data):
        self.id = data["id"]
        self.dog_id = data["dog_id"]
        self.color = data["color"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO collars (color, dog_id) VALUES (%(color)s, %(dog_id)s);"

        #Inserting collar will return ID of the new row
        collar_id = connectToMySQL("dogs_db").query_db(query, data)

        return collar_id


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM collars JOIN dogs ON dogs.id = collars.dog_id;"
        results = connectToMySQL("dogs_db").query_db(query)
        if results:
            collars = []
            #create empty list to store collars we're creating
            for row in results:
                collar = cls(row)
                data = {
                    "id": row["dogs.id"],
                    "name": row["name"],
                    "age": row["age"],
                    "hair_color": row["hair_color"],
                    "created_at": row["dogs.created_at"],
                    "updated_at": row["dogs.updated_at"]
                }
                collar.dog = dog.Dog(data)
                collars.append(collar)
            return collars