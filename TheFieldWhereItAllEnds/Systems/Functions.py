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
            for enemy in Enemies:
                if enemy is not None:
                    Count += 1
                    print(f"{Count}: {enemy.Name} | HP: {enemy.Health}")

            Choice = int(input("Input: "))
            if Choice == 1:
                if Enemy1 is not None:    
                    return Enemy1
            if Choice == 2:
                if Enemy2 is not None:
                    return Enemy2
            if Choice == 3:
                if Enemy3 is not None:
                    return Enemy3
        except:
            Timed_Text('Please choose a number!!!',0.03,True,True)
    

def Initiate_Fight(Local_Player,Ally1,Ally2,Ally3,Ally4,Enemy1,Enemy2,Enemy3):
    while True:
        if Local_Player.IsDied() == True:
            return False 
    
        
        
        if Ally1 is not None:
            Ally1.Status_Ending()
            if Ally1.IsDied() == True:
                Local_Player.Damage_Player(1)
        if Ally2 is not None: 
            Ally2.Status_Ending()
            if Ally2.IsDied() == True:
                Local_Player.Damage_Player(1)
        if Ally3 is not None: 
            Ally3.Status_Ending()
            if Ally3.IsDied() == True:
                Local_Player.Damage_Player(1)
        if Ally4 is not None: 
            Ally4.Status_Ending()
            if Ally4.IsDied() == True:
                Local_Player.Damage_Player(1)

        Selected_Unit = Local_Player.SelectUnit(Ally1,Ally2,Ally3,Ally4)
        if Selected_Unit == 1:
            Ally1.Action(Enemy1,Enemy2,Enemy3)

        if Selected_Unit == 2:
            Ally2.Action(Enemy1,Enemy2,Enemy3)
            if Ally1.IsDied() == True:
                Local_Player.Take_Damage(1)
        if Selected_Unit == 3:
            Ally3.Action(Enemy1,Enemy2,Enemy3)
            if Ally1.IsDied() == True:
                Local_Player.Take_Damage(1)
        if Selected_Unit == 4:
            Ally4.Action(Enemy1,Enemy2,Enemy3)
            if Ally1.IsDied() == True:
                Local_Player.Take_Damage(1)
        count = 0


        Timed_Text("Enemies turn!",0.03,True,True)
        if Enemy1 is not None:
            Enemy1.Action(Ally1,Ally2,Ally3,Ally4)
            count += 1
            if Enemy1.IsDied() == True:
                Enemy1 = None
                count -= 1
        if Enemy2 is not None:
            Enemy2.Action(Ally1,Ally2,Ally3,Ally4)
            count += 1
            if Enemy2.IsDied() == True:
                Enemy2 = None
                count -= 1
        if Enemy3 is not None:
            Enemy3.Action(Ally1,Ally2,Ally3,Ally4)
            count += 1
            if Enemy3.IsDied() == True:
                Enemy3 = None
                count -= 1
        if count == 0:
            return True
