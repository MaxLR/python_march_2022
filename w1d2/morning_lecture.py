from datetime import date

# BASE CLASS
class Animal:
    def __init__(self, color, name, age, size = "small", favorite_food="steak"):
        self.color = color
        self.size = size
        self.name = name
        self.favorite_food = favorite_food
        self.age = age
    
    #METHODS (actions that the instances of the class can take)
    def sleep(self):
        print(f"{self.name} is sleeping")


    def eat(self):
        print(f"{self.name} eats its favorite food: {self.favorite_food}")


    def birthday(self):
        print(f"Today is {self.name}'s birthday!")
        self.age += 1


    #CLASS METHOD
    @classmethod
    def age_from_birth_year(cls, color, name, birth_year, size="small", favorite_food="steak"):
        return cls(color, name, date.today().year - birth_year, size, favorite_food)


    #STATIC METHOD
    @staticmethod
    def is_older_than_10(age):
        return age > 10


# Creating instances of animals
my_cat = Animal("grey & white", "kiwi", "1", favorite_food="pizza")
second_cat = Animal(name = "Bootsie", age = "13", color = "black & white", size = "small")

# print(my_cat.favorite_food)

# print(f"My cat's name is {my_cat.name}, it is a {my_cat.size} cat, and the colors are {my_cat.color}")


my_cat.eat()


mr_cat = Animal.age_from_birth_year("brown & grey", "Mister", 2019)

print(mr_cat.age)
mr_cat.birthday()
print(mr_cat.age)

print(Animal.is_older_than_10(mr_cat.age))




#SUBCLASS
class Dog(Animal):
    def __init__(self, color, name, age, size = "small", favorite_food="steak", favorite_toy="ball"):
        super().__init__(color, name, age, size, favorite_food)
        self.favorite_toy = favorite_toy

    def bark(self):
        print(f"{self.name} barks!")


dog = Dog("black", "Remus", 6, "medium", favorite_food="pizza")

print(dog.age)
dog.birthday()
print(dog.age)

dog.bark()
print(dog.favorite_toy)