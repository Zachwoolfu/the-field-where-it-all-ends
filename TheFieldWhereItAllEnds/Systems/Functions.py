import time
import os
import random

def System_Clear():
    os.system("cls" if os.name == "nt" else "clear")
def Enter_Contunue():
    a = input("---Press enter to continue")
   

def Timed_Text(Text,DelayS,IndV,Entering):
    System_Clear()
    for Letters in str(Text):
        print(Letters,end="", flush=True)
        time.sleep(DelayS)

    if IndV == True:
        print("")
    if Entering == True:
        Enter_Contunue()

def Randomize_Enemies():
    return random.randint(1,2)

def Choose_Enemy(Enemy1,Enemy2,Enemy3):
    while True:
        try:
            print('Choose an enemy!')
            System_Clear()
            Enemies = [Enemy1, Enemy2, Enemy3]
            Count = 0
            Chosen_Enemy = None
            for enemy in Enemies:
                if enemy is not None:
                    Count += 1
                    print(f"{Count}: {enemy.Name} | HP: {enemy.Health}")
    
            Choice = int(input("Input: "))
            L_Count = 0
            for enemy in Enemies:
                if enemy is not None:
                    L_Count += 1
                    if Choice == L_Count:
                        Chosen_Enemy = enemy
                        return Chosen_Enemy
        except:
            Timed_Text('Please choose a number!!!',0.03,True,True)
    
def CheckIfPlrDead(Local_Player):
    if Local_Player.IsDied() == True:
            return False 
def CheckIfenemyDead(count):
    if count == 0:
            return True
def Initiate_Fight(Local_Player,Ally1,Ally2,Ally3,Ally4,Enemy1,Enemy2,Enemy3):
    while True:
        
        CheckIfPlrDead(Local_Player)
        count = 0
        
        
        if Enemy1 is not None:
            count += 1
            if Enemy1.IsDied() == True:
                Enemy1 = None
                count -= 1
        if Enemy2 is not None:
            count += 1
            if Enemy2.IsDied() == True:
                Enemy2 = None
                count -= 1
        if Enemy3 is not None:
            count += 1
            if Enemy3.IsDied() == True:
                Enemy3 = None
                count -= 1

        CheckIfenemyDead(count)
        if Ally1 is not None:
            Ally1.Stamina = Ally1.MaxStamina
            Ally1.Status_Ending()
            if Ally1.IsDied() == True:
                Local_Player.Damage_Player(1)
        else:
            Local_Player.Damage_Player(1)
        if Ally2 is not None: 
            Ally2.Stamina = Ally2.MaxStamina
            Ally2.Status_Ending()
            if Ally2.IsDied() == True:
                Local_Player.Damage_Player(1)
        else:
            Local_Player.Damage_Player(1)
        if Ally3 is not None: 
            Ally3.Stamina = Ally3.MaxStamina
            Ally3.Status_Ending()
            if Ally3.IsDied() == True:
                Local_Player.Damage_Player(1)
        else:
            Local_Player.Damage_Player(1)
        if Ally4 is not None: 
            Ally4.Stamina = Ally4.MaxStamina
            Ally4.Status_Ending()
            if Ally4.IsDied() == True:
                Local_Player.Damage_Player(1)
        else:
            Local_Player.Damage_Player(1)
        
        while True:
            Selected_Unit = Local_Player.SelectUnit(Ally1,Ally2,Ally3,Ally4)

            if Selected_Unit == 5:
                break

            AllyList = [Ally1, Ally2, Ally3, Ally4]

            if 1 <= Selected_Unit <= 4:
                Ally = AllyList[Selected_Unit - 1]

                if Ally is None:
                    continue

                if Ally.Stamina <= 0:
                    Timed_Text(f"{Ally.Name} is too tired, please wait...",0.03,True,True)
                    continue

                if Ally.IsDied():
                    Local_Player.Take_Damage(1)
                else:
                    Ally.Action(Enemy1,Enemy2,Enemy3)

                continue       
            
        

        if Enemy1 is not None:
            count += 1
            if Enemy1.IsDied() == True:
                Enemy1 = None
                count -= 1
        if Enemy2 is not None:
            count += 1
            if Enemy2.IsDied() == True:
                Enemy2 = None
                count -= 1
        if Enemy3 is not None:
            count += 1
            if Enemy3.IsDied() == True:
                Enemy3 = None
                count -= 1

        CheckIfPlrDead(Local_Player)
        CheckIfenemyDead(count)
        Timed_Text("Enemies turn!",0.03,True,True)
        if Enemy1 is not None:
            Enemy1.Action(Ally1,Ally2,Ally3,Ally4)
        if Enemy2 is not None:
            Enemy2.Action(Ally1,Ally2,Ally3,Ally4)
        if Enemy3 is not None:
            Enemy3.Action(Ally1,Ally2,Ally3,Ally4)

        CheckIfenemyDead(count)
        CheckIfPlrDead(Local_Player)
