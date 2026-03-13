class Entity:
    def __init__(self):
        print("entity is created")

    def attack(self):
        print(f"attack. Damage is {self.damage}")

class Monster(Entity):
    def __init__(self,health,damage): #is this like a constructor
        print("entity is created")
        self.damage = damage
        self.health= health
    
    def __repr__(self):
        return f"a monster with {self.health} hp"

monster = Monster(100,10)
print(monster.health)
monster.attack()

print(monster)


    

