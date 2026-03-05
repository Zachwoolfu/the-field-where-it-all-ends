from Systems.Functions import Timed_Text
from Systems.Class import ClassDescript
class Units:
    def __init__(self,Name,Class):
        self.Name = Name
        self.MaxHealth = 5
        self.Health = 5
        self.Stamina = 2 ## Base Stamina AlWAYS!!!
        self.Relationship_Status = 1  
        self.Relationshp_Level = 1
        self.Class = Class
        self.Equipement = 0


    def ClassDescript(Self):
        x = ClassDescript()
        return x
        

    def IsDied(self):
        if self.Health <= 0:
            return True

    def Take_Damage(self,Amount):
        if self.Health > 0:
            self.Health -= Amount

    def Action(Self):
        if Self.Stamina > 0:
            Timed_Text("Select an action!",0.03,True,False)
            print(Self.Name," ", end="")
            print("(",Self.ClassDescript(),")",sep="")
            
        
    
