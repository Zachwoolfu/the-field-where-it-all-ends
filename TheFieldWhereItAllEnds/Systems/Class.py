from Systems.Functions import Timed_Text
def ClassDescript(Self):
       
        ClassType = " "
        if Self.Class == 1:
            ClassType = "Mage"
        if Self.Class == 2:
            ClassType = "Warrior"
        if Self.Class == 3:
            ClassType = "Hunter"

        if ClassType == 11:
            ClassType = "Deduction Of Infinity"
        if ClassType == 12:
            ClassType = "Eternal Suffering"
        if ClassType == 13:
            ClassType = "Our Lord reincarnate"

        if ClassType == 21:
            ClassType = "To it’s Absolution"
        if ClassType == 22:
            ClassType = "Species of Annihilation"
        if ClassType == 23:
            ClassType = "Reprise of the void"

        if ClassType == 31:
            ClassType = "Dissonant Courage"
        if ClassType == 32:
            ClassType = "The Holy unjust"
        if ClassType == 33:
            ClassType = "Unwritten melodies"
        return ClassType

def Class_Ability_Cast(ClassType,AbilityType):
    if ClassType == "Mage":
        if AbilityType == 1:
            print("MAGICM IZZLE PEW PEW!")
        if AbilityType == 2:
            print("WARPING TO THE ENEMY AND BACK!")

def Class_Ability_Description(ClassType):
    if ClassType == "Mage":
        print("1: Magic Missile: Deal 1 Magic damage in a close to medium range")
        print("2: Warp: Teleport instantly to a space.")
    
    print("Input:",end="")
    Given_Input = 0
    while True:
        try:
            Given_Input = int(input(" "))
            return Class_Ability_Cast(ClassType,Given_Input)
        except TypeError:
            Timed_Text("Something sent wrong, please try again! ",0.03,True,True)
    
    


