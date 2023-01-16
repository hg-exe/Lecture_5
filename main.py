import random

class Collectable:
    total_points = 0

    def __init__(self, name):
        self.name =  name
        self.value = 0

    def Collect(self):
        Collectable.total_points += self.value

class Coin(Collectable):

    def __init__(self, name, value):
        Collectable.__init__(self, name)
        self.value = value
    pass

class Potion(Collectable):
    colours = ["Red", "Blue", "Green", "Yellow"]
    def __init__(self, name, value):
        Collectable.__init__(self, name)
        self.value = value
        self.colour = random.choice(Potion.colours)





#tgame code
while Collectable.total_points < 300:
    choice = input("Enter a number between 1 and 6")
    if not choice.isdigit():
        print("That is not a number, you failed")
        break
    if choice.int() > 6:
        print("That number is too high")
        break
    if choice.int() <=3:
        coin = Coin("A coin...", 50)
        coin.collect()
    #elif:



