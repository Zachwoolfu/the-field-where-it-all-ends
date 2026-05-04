from Systems.Functions import Timed_Text
from Systems.Functions import Choose_Enemy
import random
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

def Class_Ability_Cast(Self,AbilityType,Enemy1,Enemy2,Enemy3):
    ClassType = ClassDescript(Self)
    if ClassType == "Mage":
        if AbilityType == 1:
            Self.Stamina -= 1
            Enemy_Choice = Choose_Enemy(Enemy1,Enemy2,Enemy3)
            Damage_Calc = Self.Strength - Enemy_Choice.Magic_Defense
            RandomNum = random.randint(1,100)
            if Enemy_Choice.Dash <= 0:
                if Enemy_Choice.Dodge <= RandomNum:
                    if Damage_Calc < 0:
                        Damage_Calc = 0
                        Timed_Text("Damage Mitigated!",0.03,True,True) 
                    else:
                        Timed_Text(f"{Self.Name} Fires a quick magic missile at {Enemy_Choice.Name} "
                        f"Dealing -{Damage_Calc} Magic damage",0.03,True,True)
                        Enemy_Choice.Damage_Enemy(Damage_Calc)
                else:
                    Timed_Text("Enemy Dodges!!",0.03,True,True)
            else:
                Enemy_Choice.Success_Dash()
        if AbilityType == 2:
            Self.Stamina -= 1
            Timed_Text(f"{Self.Name} magic tingles, preparing a warp...",0.03,True,True)
            Self.Dash += 1
    if ClassType == "Warrior":
        if AbilityType == 1:
            Self.Stamina -= 1
            Enemy_Choice = Choose_Enemy(Enemy1,Enemy2,Enemy3)
            Damage_Calc = Self.Strength - Enemy_Choice.Physical_Defense
            RandomNum = random.randint(1,100)
            if Enemy_Choice.Dash <= 0:
                if Enemy_Choice.Dodge <= RandomNum:
                    if Damage_Calc < 0:
                        Damage_Calc = 0
                        Timed_Text("Damage Mitigated!",0.03,True,True) 
                    else:
                        Timed_Text(f"{Self.Name} Slashes at {Enemy_Choice.Name} Dealing -{Damage_Calc} Physical damage",0.03,True,True) 
                        Enemy_Choice.Damage_Enemy(Damage_Calc)
                else:
                    Timed_Text("Enemy Dodges!!",0.03,True,True)
            else:
                Enemy_Choice.Success_Dash()
        if AbilityType == 2:
            Self.Stamina -= 1
            Timed_Text(f"{Self.Name} raises their shield!",0.03,True,True)
            if "WarriorAbility2" in Self.Applied_Status:
                Timed_Text(f"Block duration Refreshed!",0.03,True,True)
                Self.Applied_Status["WarriorAbility2"] = 1
            else:
                Self.Defence += 2
                Self.Applied_Status["WarriorAbility2"] = 1
        if ClassType == "Hunter":
            if AbilityType == 1:
                Self.Stamina -= 1
                Enemy_Choice = Choose_Enemy(Enemy1,Enemy2,Enemy3)
                Damage_Calc = Self.Strength - Enemy_Choice.Physical_Defense
                Damage_Calc = Self.Strength - Enemy_Choice.Physical_Defense
                RandomNum = random.randint(1,100)
                if Enemy_Choice.Dash <= 0:
                    if Enemy_Choice.Dodge <= RandomNum:
                        if Damage_Calc < 0:
                            Damage_Calc = 0
                            Timed_Text("Damage Mitigated!",0.03,True,True) 
                        else:
                            Timed_Text(f"{Self.Name} Slashes at {Enemy_Choice.Name} Dealing -{Damage_Calc} Physical damage",0.03,True,True) 
                            Enemy_Choice.Damage_Enemy(Damage_Calc)
                    else:
                        Timed_Text("Enemy Dodges!!",0.03,True,True)
                else:
                    Enemy_Choice.Success_Dash()
        if ClassType == "Deduction Of Infinity":
            if AbilityType == 1:
                print("gonna add later x-p")


def Class_Ability_Description(Self):
    ClassType = ClassDescript(Self)
    if ClassType == "Mage":
        print(f"1: Magic Missile: Deal {Self.Strength} Magic damage to a target")
        print("2: Warp: Teleport instantly to dodge the next damage taken.")
        if Self.Dash > 0:
            print(f"Active Warps: {Self.Dash}")

    if ClassType == "Warrior":
        print(f"1: Slash: Deal {Self.Strength} Physical Damage to a single target")
        print("2: Block: Gain -2 damage reduction for 2 rounds")      
        if "WarriorAbility2" in Self.Applied_Status:
            print("Active Buff: Has +2 defence")
    if ClassType == "Hunter":
        print(f"1: Slash: Deal {Self.Strength} Physical Damage to a single target")      
        print("Passively gain 25% Dodge Chance")
    if ClassType == "Deduction Of Infinity":
        print("1: Addition: Summon an addition sign. After a round it will activate and home towards the Targeted enemy")
        print("2: Multiply: [Integer] Stacks on enemies by x2")
        print(f"3: Subtraction: Consume an [Integer] stack on a single target to deal {Self.Strength} magic damage")
        print(f"4: Division: Consume 1/2 [Integer] stack on a single target to deal {Self.Strength} damage multiplied by stack number")

    if ClassType == "Eternal Suffering":
        print(f"1: Earth's torment: Creates a magma zone dealing {Self.Strength} magic damage for 3 rounds")
        print(f"2: Suffocation: Inflict a burn, reducing Magic resistance by {Self.Strength}/2")

    if ClassType == "Our Lord reincarnate":
        print("1: Plague's eternal Cure: Cleanse all allies of negative effects")
        print(f"2: God's left hand: Deal {Self.Strength} magic damage to all enemies")

    if ClassType == "To it’s Absolution":
        print("1: Aggression: Gain 75% damage mitigation this round. Damage taken increases your next attack")
        print("2: Annoyance: Force all enemies to target you for 1 round")
        print(f"3: Clean cut: Deal {Self.Strength} Physical damage to all enemies")

    if ClassType == "Species of Annihilation": 
        print(f"1: Blood draw: Lose HP to increase physical damage by +{Self.Strength}")
        print(f"2: Eradicate: Deal {Self.Strength} damage to all enemies")
        print(f"3: Chains of Dissonance: Deal {Self.Strength} damage and apply execution mark")

    if ClassType == "Reprise of the void":
        print(f"1: Vibration: Deal {Self.Strength} physical damage and silence target")
        print("2: Dissociate: Turn invisible for 3 rounds (immune until action)")
        print(f"3: nil: Silence all enemies and reduce defenses by {Self.Strength}/2 for 3 rounds")

    if ClassType == "Dissonant Courage":
        print(f"1: Courage: Increase all allies damage by +{Self.Strength}")
        print(f"2: Arrow of recursion: Start at {Self.Strength} damage, decreasing each round")
        print("3: Redo: Refresh an ally's cooldown")

    if ClassType == "The Holy unjust":
        print(f"1: Holy lyre: Deal {Self.Strength} magic damage to all enemies")
        print(f"2: Wings of protection: Shield scales with {Self.Strength}")
        print(f"3: Warm embrace: Heal an ally for {Self.Strength}+ HP")

    if ClassType == "Unwritten melodies":
        print(f"1: Wishing Star: Deal {Self.Strength} magic damage to a target")
        print("2: Constellation: Generate stars that enhance Wishing Star")
        print("3: Eyes of the Galaxy: Refresh Wishing Star cooldown")
        print("Input:",end="")
        Given_Input = 0
    while True:
        try:
            Given_Input = int(input(" "))
            
            return Given_Input
        except:
            Timed_Text("Something sent wrong, please try again! ",0.03,True,True)
    
    


