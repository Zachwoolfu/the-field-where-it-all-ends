class Enemy:
    def __init__(self,Type):
        self.Type = Type
        self.Strength = 1
        self.MaxHealth = 1
        self.Stamina = 1
        self.Health = 1 ## Howmuch units have fallen!
        self.Magic_Defense = 0
        self.Physical_Defense = 0
        if Type == 1:
            self.Strength = 1
            self.MaxHealth = 2
            self.Health = 2
        elif Type == 2:
            self.Strength = 2
            self.MaxHealth = 3
            self.Health = 3
        


    def Damage_Enemy(self, amount):
        self.Health -= amount
        
    def IsDied(self):
        if self.Health <= 0:
            return True
