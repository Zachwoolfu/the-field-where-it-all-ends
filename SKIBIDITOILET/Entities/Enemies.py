class Enemies:
    def __init__(self, name):
        self.name = name
        self.MaxHealth = 1
        self.Health = 1 ## Howmuch units have fallen!


    def Damage_Enemy(self, amount):
        self.Health -= amount
        
    def IsDied(self):
        if self.Health <= 0:
            return True
