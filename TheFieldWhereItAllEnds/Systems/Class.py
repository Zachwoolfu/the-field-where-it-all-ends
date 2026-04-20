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

def Class_Ability_Cast(Self,AbilityType,Enemy1,Enemy2,Enemy3):
    ClassType = ClassDescript(Self)
    if ClassType == "Mage":
        if AbilityType == 1:
            print("MAGICM IZZLE PEW PEW!")
       
        if AbilityType == 2:
            print("WARPING TO THE ENEMY AND BACK!")
       
def Class_Ability_Description(Self):
    ClassType = ClassDescript(Self)
    if ClassType == "Mage":
        print("1: Magic Missile: Deal 1 Magic damage to a close - medium range target")
        print("2: Warp: Teleport instantly to dodge the next damage taken.")
    if ClassType == "Warrior":
        print("1: Slash: Deal 1 Physical Damage to a close range target")
        print("2: Block: Gain 50% damage reduction for this round")      
    if ClassType == "Hunter":
        print("1: Slash: Deal 1 Physical Damage ot a close range target")      
    if ClassType == "Deduction Of Infinity":
        print("1: Addition: Summon an addition sign. After a round it will activate and home towards the Targeted enemy")
        print("2: Multiply: [Integer] Stacks on enemies by x2")
        print("3: Subtraction: Consume an [Integer] stack on a singe target to deal 2 magic damage")
        print("4: Division: Consume 1/2 [Integer] stack on a singe target to deal 1 damage multiply by stack number")
    if ClassType == "Eternal Suffering":
        print("1: Earth's torment: Erupts a vulcano, creating a magma zone, dealing 1 magic damage to enemies for 3 rounds")
        print("2: Suffication: Inflice a burn to a single target, deducing their Magic resistence by 1/2")
    if ClassType == "Our Lord reincarnate":
        print("1: Plague's eternal Cure: Cleans you and all allies in your team of all negative effects")
        print("2: God's left hand: Drop down gods had to deal 1 magic damage to all enemies in the field")

    if ClassType == "To it’s Absolution":
        print("1: Aggression: Grant yourself 75% damage mitigation for this round. Damage taken will increase your next damage to increase.")
        print("2: Annoyance: Force all enemies to focus you for 1 round")
        print("3: Clean cut: Bring out your blae, and slice, dealing 1 Physical damage to all enemies in the field")
    if ClassType == "Species of Annihilation": 
        print("1: Blood draw: Deduce your current health to increase you physical damage by +1")
        print("2: Eradicate: Deal damage to all enemies")
        print("3: Chains of Dissoance: Deal damage to a single enemy, marking them with [execution] for 5 rounds, if the stack detects them at less then 2 hp, They are executed and you are healed.")
    if ClassType == "Reprise of the void":
        print("1: Vibration: Deal 1 physical damage to a singe target, silencing them from using an ability this round.")
        print("2: Dissociate: Turn invisible for 3 rounds, becoming immune to all damage. Actions will exit invisibility")
        print("3: nil: Silence all enemies from casting and attacking, deducing their defences by 1/2, lasting for 3 rounds")
    if ClassType == "Dissonant Courage":
        print("1: Courage: Increase you and all allie's damage by +1")
        print("2: Arrow of recursion: Deal 3 physical damage to a single target, each round it will deal damage again, dealing -1 less for each damage dealt")
        print("3: Redo: Refresh an allies cooldown")
    if ClassType == "The Holy unjust":
        print("1: Holy lyre: Dealing 1 magic damage to all enemies, reducing their physical defences by 1/4")
        print("2: Wings of protection: Grant you or an ally a shied scaling off of your 1/4 max health")
        print("3: Warm embrace: Heal an ally 1+ hp")
    if ClassType == "Unwritten melodies":
        print("1: Wishing Star: Deal 1 magic damage to a single target.")
        print("2: Constellation: Forge a random of 1-4 stars to spiral around you, Casting {Wishing Star} will fire all stars the target, dealing 1+ damage each star")
        print("3: Eyes of the Galaxy: Refresh wishing Star Cool-Down")

    print("Input:",end="")
    Given_Input = 0
    while True:
        try:
            Given_Input = int(input(" "))
            
            return Given_Input
        except TypeError:
            Timed_Text("Something sent wrong, please try again! ",0.03,True,True)
    
    


