from Systems.Functions import Timed_Text
import random

class Enemy:
    def __init__(self,Type):
        self.Type = Type
        self.Name = "Enemy"
        self.Strength = 1
        self.MaxHealth = 1
        self.Stamina = 1
        self.Health = 1 ## Howmuch units have fallen!
        self.Magic_Defense = 0
        self.Physical_Defense = 0
        if Type == 1:
            self.Name = "Enemy1"
            self.Strength = 1
            self.MaxHealth = 2
            self.Health = 2
        elif Type == 2:
            self.Name = "Enemy2"
            self.Strength = 2
            self.MaxHealth = 3
            self.Health = 3

    def Heal_Enemy(self,amount):
        if self.MaxHealth > self.Health:
            self.Health += amount
        else:
            self.Health = self.MaxHealth
    def Damage_Enemy(self, amount):
        if self.MaxHealth > self.Health:
            self.Health -= amount
        else:
            self.Health = self.MaxHealth
        
    def IsDied(self):
        if self.Health <= 0:
            return True

    def Action(self,Ally1,Ally2,Ally3,Ally4):
        print(f"{self.Name} Attacks!")
        count = 0
        if Ally1 is not None:
            count += 1
        if Ally2 is not None:
            count += 1
        if Ally3 is not None:
            count += 1
        if Ally4 is not None:
            count += 1
        Randomized = random.randint(1,count)
        ChosenAlly = None
        if Randomized == 1:
            if Ally1 is not None:
                ChosenAlly = Ally1
        if Randomized == 2:
            if Ally2 is not None:
                ChosenAlly = Ally2
        if Randomized == 3:
            if Ally3 is not None:
                ChosenAlly = Ally3
        if Randomized == 4:
            if Ally4 is not None:
                ChosenAlly = Ally4
        
        Timed_Text(f"{self.Name} Attacks {ChosenAlly.Name} for -{self.Strength} damage!",0.03,True,True)
        ChosenAlly.Take_Damage(self.Strength)
        
