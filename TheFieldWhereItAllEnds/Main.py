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
            Timed_Text('Give Class: ',0.03,False,False)
            Given_Class = int(input(" "))
            Ally1 = Units(Given_Name,Given_Class)
            break
        except:
            print("please place in a valid name.") 

    Enemies1 = Enemy(Randomize_Enemies())
    Enemies2 = Enemy(Randomize_Enemies())
    Enemies3 = Enemy(Randomize_Enemies())
    
    Initiate_Fight(Local_Player,Ally1,Ally2,Ally3,Ally4,Enemies1,Enemies2,Enemies3)

Starting_Dialogue()
