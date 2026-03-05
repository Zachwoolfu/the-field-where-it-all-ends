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



def Class_Ability():
    print("WAAAAHHH")