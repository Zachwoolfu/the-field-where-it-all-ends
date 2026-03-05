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

def Initiate_Fight(Local_Player,Ally1,Ally2,Ally3,Ally4):
    while True:
        Plr_Dead = Local_Player.IsDied()
        if Plr_Dead == True:
            return False 
        Selected_Unit = Local_Player.SelectUnit(Ally1,Ally2,Ally3,Ally4)
        if Selected_Unit == 1:
            Ally1.Action()