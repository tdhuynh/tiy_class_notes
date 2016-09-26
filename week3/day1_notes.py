class Player:
    stuff
    stuff
    stuff
    def hit_or_stand(self):
        stuff
        stuff
        stuff
        stuff

class Dealer(Player): # this will create new class Dealer with all code from Player
# this will allow you to save lines of code
    def hit_or_stand(self):
        if value < 16:
            hit
        else:
            stand

#################################


class Weapon:
    def __init__(self):
        self.damage = 0
        self.durability = 0

    def attack(self):
        self.durability -= 1
        return self.damage

class Sword(Weapon):
    def __init__(self):
        self.damage = 5
        self.durability = 10
