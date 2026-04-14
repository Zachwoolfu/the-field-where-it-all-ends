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
        Timed_Text("Your turn!",0.03,True,True)
        while True:
            try:
                Timed_Text("Select A unit! ",0.03,True,False)
                if Ally1 is not None:
                    count += 1
                    print("1:",Ally1.Name,end=" ")
                    print("(",Ally1.ClassDescript(),")", sep="")
                if Ally2 is not None:
                    count += 1
                    print("2:",Ally2.Name)
                if Ally3 is not None:
                    count += 1
                    print("3:",Ally3.Name)
                if Ally4 is not None:
                    count += 1
                    print("4:",Ally4.Name)
                print("Input: ",end="")
                Given_Input = int(input(" "))
                if 0 < Given_Input <= count:
                    return Given_Input
                else:
                    Timed_Text("Selection invalid, please inpute an available number! ",0.03,True,True)
            except:
                Timed_Text("Something sent wrong, please try again! ",0.03,True,True)

        



