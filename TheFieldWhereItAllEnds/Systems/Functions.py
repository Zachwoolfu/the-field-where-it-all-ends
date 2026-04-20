import time
import os

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
    import random
    return random.randint(1,2)

def Choose_Enemy(Enemy1,Enemy2,Enemy3):
    while True:
        try:
            Timed_Text('Choose an enemy',0.03,True,True)
            if Enemy1 == None:    
                print("1:"..Enemy1.Name)
            if Enemy2 == None:
                print("2:"..Enemy2.Name)
            if Enemy3 == None:
                print("3:"..Enemy3.Name)
            print("Input:")
            Choice = int(input("Input"))
            return Choice
        except:
            Timed_Text('Please choose a number!!!',0.03,True,True)
    return 
    

def Initiate_Fight(Local_Player,Ally1,Ally2,Ally3,Ally4,Enemy1,Enemy2,Enemy3):
    while True:
        Plr_Dead = Local_Player.IsDied()
        if Plr_Dead == True:
            return False 
        
        Selected_Unit = Local_Player.SelectUnit(Ally1,Ally2,Ally3,Ally4)
        if Selected_Unit == 1:
            Ally1.Action(Enemy1,Enemy2,Enemy3)
        if Selected_Unit == 2:
            Ally2.Action(Enemy1,Enemy2,Enemy3)
        if Selected_Unit == 3:
            Ally3.Action(Enemy1,Enemy2,Enemy3)
        if Selected_Unit == 4:
            Ally4.Action(Enemy1,Enemy2,Enemy3)

        Timed_Text("Enemies turn!",0.03,True,True)
        if Enemy1 is not None:
            Enemy1.Action(Ally1,Ally2,Ally3,Ally4)
            if Enemy1.IsDied() == true:
                Enemy1 = None
        if Enemy2 is not None:
            Enemy2.Action(Ally1,Ally2,Ally3,Ally4)
            if Enemy2.IsDied() == true:
                Enemy2 = None
        if Enemy3 is not None:
            Enemy3.Action(Ally1,Ally2,Ally3,Ally4)
            if Enemy3.IsDied() == true:
                Enemy3 = None
        
