import sys
import os
import time
from Entities.Player import Player
from Systems.Functions import Timed_Text
from Systems.Functions import Initiate_Fight
from Systems.Functions import System_Clear
from Entities.Enemies import Enemy
from Systems.Functions import Randomize_Enemies
from Entities.Units import Units


global Local_Player
global Ally1
global Ally2
global Ally3
global Ally4

Ally1 = None
Ally2 = None
Ally3 = None
Ally4 = None

Enemies1 = None
Enemies2 = None
Enemies3 = None
while True:
    try:
        Given_Name = input("Input Name:")
        Local_Player = Player(Given_Name)
        break
    except:
        print("please place in a valid name.")        



def Starting_Dialogue():
    Timed_Text('You wake up in a field of grass skibidi toilet style',0.03,True,True)
    Timed_Text('WOA SOMETHING IS IN FRONT OF YOU AHHH!!',0.03,True,True)    
    while True:
        try:
            Timed_Text('Input Ally1 Name:',0.03,False,False)
            Given_Name = input(" ")
            System_Clear()
            print("1: Mage")
            print("2: Warrior")
            print("3: Hunter")
            Given_Class = 1
            while True:
                Given_Class = int(input(" "))
                if Given_Class > 0 and Given_Class < 4:
                    break
                else:
                    Timed_Text('PLEASE PUT A VALID NUMBER!!!!',0.03,False,False)
                
            Ally1 = Units(Given_Name,Given_Class)
            break
        except:
            print("please place in a valid name.") 

    while True:
        try:
            Timed_Text('Input Ally2 Name:',0.03,False,False)
            Given_Name = input(" ")
            System_Clear()
            print("1: Mage")
            print("2: Warrior")
            print("3: Hunter")
            Given_Class = 1
            while True:
                Given_Class = int(input(" "))
                if Given_Class > 0 and Given_Class < 4:
                    break
                else:
                    Timed_Text('PLEASE PUT A VALID NUMBER!!!!',0.03,False,False)
                
            Ally2 = Units(Given_Name,Given_Class)
            break
        except:
            print("please place in a valid name.") 

    Enemies1 = Enemy(Randomize_Enemies())
    Enemies2 = Enemy(Randomize_Enemies())
    #Enemies3 = Enemy(Randomize_Enemies())
    Timed_Text('Will add a tutorial soon; play around!',0.03,True,True)    
    Timed_Text('Enemies randomized... You ready??!',0.03,True,True)    
    Completion = Initiate_Fight(Local_Player,Ally1,Ally2,Ally3,Ally4,Enemies1,Enemies2,Enemies3)
    if Completion == True:
        Timed_Text('Congratulations you win!',0.03,True,True)
    else:
        Timed_Text('You lose... Better luck next time!',0.03,True,True)
Starting_Dialogue()
