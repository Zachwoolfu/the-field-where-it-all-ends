from Systems.Functions import Timed_Text
from Systems.Class import ClassDescript
from Systems.Class import Class_Ability_Description
from Systems.Class import Class_Ability_Cast
class Units:
    def __init__(self,Name,Class):
        self.Name = Name
        self.MaxHealth = 5
        self.Health = 5
        self.Strength = 1
        self.Defence = 0 ## 0%
        self.Dodge = 0 ### 0%
        self.Dash = 0 ### 1 = if hit once it will dodge!
        self.Stamina = 2 ## Base Stamina AlWAYS!!!
        self.Distance = 3 ## ON ACTION!
        self.Relationship_Status = 1  
        self.Relationshp_Level = 1
        self.Class = Class
        self.Equipement = 0

    def ClassDescript(Self):
        x = ClassDescript(Self)
        return x
        

    def IsDied(self):
        if self.Health <= 0:
            return True

    def Take_Damage(self,Amount):
        if self.Health > 0:
            self.Health -= Amount

    def Action(Self,Enemy1,Enemy2,Enemy3):
        if Self.Stamina > 0:
            Timed_Text("Select an action!",0.03,True,False)
            print(Self.Name," ", end="")
            print("(",ClassDescript(Self),")",sep="")
            ChoseAbility = Class_Ability_Description(Self)
            Class_Ability_Cast(Self,ChoseAbility,Enemy1,Enemy2,Enemy3)
    

            
            
            
        
    
