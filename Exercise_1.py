import random


class Enemy:
    weapons = {"Sword": 5, "MorningStar": 8, "Bow": 10}

    # Challenge
    names = ["Edwin", "Mikhaeel", "Manan", "Katie", "Adam", "Benjamin"]
    homelands = ["the Gaskell building", "Rivendell", "the bins", "a very slightly different dimension", "Luton"]
    abilities = ["Blizzard", "Seduce", "Annoy", "Gaslight", "Gatekeep", "Girlboss", "Fireball"]
    adjectives = [" tired" "brave", "accomplished", "legendary", "lonely", "pesky", "scary", "fearsome", "sleepy"]
    professions = ["sailor", "farmer", "henchman", "prostitute", "barkeep", "wizard", "games designer", "bat"]

    def __init__(self, name, homeland, ability):
        self.bio = None
        self.weapon = None
        self.name = name
        self.homeland = homeland
        self.ability = ability

    def Set_Bio(self, bio):
        if not isinstance(bio, str):
            print("Bio must be a string")
            return
        self.bio = bio

    def Get_Bio(self):
        return self.bio

    def Equip_Random_Weapon(self):
        self.weapon = random.choice(list(Enemy.weapons.items()))


# Printing enemy fields
enemy1 = Enemy("Bob", "Frostwolves", "Enrage")
print(vars(enemy1))
enemy2 = Enemy("Cat", "Beer-kegs", "Drunken Master")
print(vars(enemy2))

# Challenge
Enemies = []
for i in range(5):
    name = Enemy.names[i]
    homeland = random.choice(Enemy.homelands)
    ability = random.choice(Enemy.abilities)
    enemy = Enemy(name, homeland, ability)
    enemy.Equip_Random_Weapon()
    enemy.Set_Bio("{} is a {} {} from {}, specialising in using their {} technique to defeat their opponents".format(name, random.choice(Enemy.adjectives), random.choice(Enemy.professions), homeland, ability))
    print(enemy.Get_Bio())
    Enemies.append(enemy)
