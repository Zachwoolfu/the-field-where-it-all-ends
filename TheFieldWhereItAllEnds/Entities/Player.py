import time
from Systems.Functions import Timed_Text
from Systems.Functions import System_Clear
class Player:
    def __init__(self, name):
        self.name = name
        self.MaxHealth = 1
        self.Health = 1 ## Howmuch units have fallen!

    def Damage_Player(self, amount):
        self.Health -= amount
    
    def IsDied(self):
        if self.Health <= 0:
            return True

    def SelectUnit(self,Ally1, Ally2,Ally3,Ally4):
        count = 0
        print("Your turn!")
        while True:
            try:
                Timed_Text("Select A unit! (Or type '5' to finish) ",0.03,True,False)
                Allies = [Ally1, Ally2, Ally3, Ally4]

                for ally in Allies:
                    if ally is not None:
                        count += 1
                        print(f"{count}: {ally.Name} | HP: {ally.Health} | {ally.ClassDescript()}")
             
                print("Input: ",end="")
                Given_Input = int(input(" "))
                if 0 < Given_Input <= count:
                    return Given_Input
                elif Given_Input == 5:
                    return "end"
                else:
                    Timed_Text("Selection invalid, please inpute an available number! ",0.03,True,True)
            except ValueError:
                Timed_Text("Something sent wrong, please try again! ",0.03,True,True)
