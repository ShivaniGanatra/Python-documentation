# a basic class
class Person:
    eye_colour = "hazel"
    hair_colour = "brown"

    def walk(self): # have to put parameter but can be anything self refers to the instnace of the class
        print("walking")
    def talk_to(self,person):
        print(f'talks to {person}')

# create an instance
shivani = Person()
print(shivani.eye_colour)
print(shivani.hair_colour)
shivani.walk()
shivani.talk_to("Khushi")

# __init__ dunder function
class Mage:
    def __init__(self,health, mana):
        self.health = health
        self.mana = mana
        print("the mage class was created")
        print(self.health)
    
    def __len__(self):
        return self.health
    
    def attack(self,target):
        target.health -=10

class Monster:
    health = 40
    
mage = Mage(100,200)
print(len(mage))
monster = Monster()
print(monster.health)
mage.attack(monster)
print(monster.health)
# the mage class was created
# 100
# 100
