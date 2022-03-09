
#GAME CLASS

class Game:
    def __init__(self):
        self.player1 = ""
        self.player2 = ""

    def play_round(self):
        pass


class Player:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.attacks = []
        self.health = 100

    def attack(self, target):
        pass


max = Player("max", "ninja")
christian = Player("christian", "pirate")

christian.attack(max)