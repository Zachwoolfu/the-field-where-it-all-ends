from Systems.Functions import Timed_Text
from Systems.Functions import Choose_Enemy
import random
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

    if Self.Class == 11:
        ClassType = "Deduction Of Infinity"
    if Self.Class == 12:
        ClassType = "Eternal Suffering"
    if Self.Class == 13:
        ClassType = "Our Lord reincarnate"

    if Self.Class == 21:
        ClassType = "To it’s Absolution"
    if Self.Class == 22:
        ClassType = "Species of Annihilation"
    if Self.Class == 23:
        ClassType = "Reprise of the void"

    if Self.Class == 31:
        ClassType = "Dissonant Courage"
    if Self.Class == 32:
        ClassType = "The Holy unjust"
    if Self.Class == 33:
        ClassType = "Unwritten melodies"

    return ClassType


def Class_Ability_Cast(Self, AbilityType, Enemy1, Enemy2, Enemy3):

    Enemies = [Enemy1, Enemy2, Enemy3]
    Enemies = [Enemy for Enemy in Enemies if Enemy != None]

    ClassType = ClassDescript(Self)

    # =========================================================
    #           MAGE: magic 
    # =========================================================

    if ClassType == "Mage":

        if AbilityType == 1:
            Self.Stamina -= 1

            Enemy_Choice = Choose_Enemy(Enemy1, Enemy2, Enemy3)

            Damage_Calc = Self.Strength - Enemy_Choice.Magic_Defense
            RandomNum = random.randint(1, 100)

            if Enemy_Choice.Dash <= 0:

                if Enemy_Choice.Dodge <= RandomNum:

                    if Damage_Calc < 0:
                        Damage_Calc = 0
                        Timed_Text("Damage Mitigated!", 0.03, True, True)

                    else:
                        Timed_Text(
                            f"{Self.Name} Fires a quick magic missile at "
                            f"{Enemy_Choice.Name} dealing "
                            f"-{Damage_Calc} magic damage",
                            0.03,
                            True,
                            True
                        )

                        Enemy_Choice.Damage_Enemy(Damage_Calc)

                else:
                    Timed_Text("Enemy Dodges!!", 0.03, True, True)

            else:
                Enemy_Choice.Success_Dash()

        if AbilityType == 2:
            Self.Stamina -= 1

            Timed_Text(
                f"{Self.Name} magic tingles, preparing a warp...",
                0.03,
                True,
                True
            )

            Self.Dash += 1

    # =========================================================
    # WARRIOR
    # =========================================================

    if ClassType == "Warrior":

        if AbilityType == 1:

            Self.Stamina -= 1

            Enemy_Choice = Choose_Enemy(Enemy1, Enemy2, Enemy3)

            Damage_Calc = Self.Strength - Enemy_Choice.Physical_Defense
            RandomNum = random.randint(1, 100)

            if Enemy_Choice.Dash <= 0:

                if Enemy_Choice.Dodge <= RandomNum:

                    if Damage_Calc < 0:
                        Damage_Calc = 0
                        Timed_Text("Damage Mitigated!", 0.03, True, True)

                    else:
                        Timed_Text(
                            f"{Self.Name} Slashes at "
                            f"{Enemy_Choice.Name} dealing "
                            f"-{Damage_Calc} physical damage",
                            0.03,
                            True,
                            True
                        )

                        Enemy_Choice.Damage_Enemy(Damage_Calc)

                else:
                    Timed_Text("Enemy Dodges!!", 0.03, True, True)

            else:
                Enemy_Choice.Success_Dash()

        if AbilityType == 2:

            Self.Stamina -= 1

            Timed_Text(
                f"{Self.Name} raises their shield!",
                0.03,
                True,
                True
            )

            if "WarriorAbility2" in Self.Applied_Status:

                Timed_Text(
                    "Block duration refreshed!",
                    0.03,
                    True,
                    True
                )

                Self.Applied_Status["WarriorAbility2"] = 1

            else:
                Self.Defence += 2
                Self.Applied_Status["WarriorAbility2"] = 1

    # =========================================================
    # HUNTER
    # =========================================================

    if ClassType == "Hunter":

        if AbilityType == 1:

            Self.Stamina -= 1

            Enemy_Choice = Choose_Enemy(Enemy1, Enemy2, Enemy3)

            Damage_Calc = Self.Strength - Enemy_Choice.Physical_Defense
            RandomNum = random.randint(1, 100)

            if Enemy_Choice.Dash <= 0:

                if Enemy_Choice.Dodge <= RandomNum:

                    if Damage_Calc < 0:
                        Damage_Calc = 0

                        Timed_Text(
                            "Damage Mitigated!",
                            0.03,
                            True,
                            True
                        )

                    else:
                        Timed_Text(
                            f"{Self.Name} fires an arrow at "
                            f"{Enemy_Choice.Name} dealing "
                            f"-{Damage_Calc} physical damage",
                            0.03,
                            True,
                            True
                        )

                        Enemy_Choice.Damage_Enemy(Damage_Calc)

                else:
                    Timed_Text("Enemy Dodges!!", 0.03, True, True)

            else:
                Enemy_Choice.Success_Dash()

    # =========================================================
    # DEDUCTION OF INFINITY #FROM MAGE
    # =========================================================

    if ClassType == "Deduction Of Infinity":

        # Addition
        if AbilityType == 1:

            Self.Stamina -= 1

            Enemy_Choice = Choose_Enemy(Enemy1, Enemy2, Enemy3)

            if "Integer" not in Enemy_Choice.Applied_Status:
                Enemy_Choice.Applied_Status["Integer"] = 0

            Enemy_Choice.Applied_Status["Integer"] += 1

            Damage_Calc = Self.Strength - Enemy_Choice.Magic_Defense

            if Damage_Calc < 0:
                Damage_Calc = 0

            Timed_Text(
                f"{Self.Name} summons an Addition sign on "
                f"{Enemy_Choice.Name}!",
                0.03,
                True,
                True
            )

            Timed_Text(
                f"{Enemy_Choice.Name} gains an Integer stack!",
                0.03,
                True,
                True
            )

            Enemy_Choice.Damage_Enemy(Damage_Calc)

        # Multiply
        if AbilityType == 2:

            Self.Stamina -= 1

            Enemy_Choice = Choose_Enemy(Enemy1, Enemy2, Enemy3)

            if "Integer" in Enemy_Choice.Applied_Status:

                Enemy_Choice.Applied_Status["Integer"] *= 2

                Timed_Text(
                    f"{Self.Name} multiplies "
                    f"{Enemy_Choice.Name}'s Integer stacks!",
                    0.03,
                    True,
                    True
                )

            else:
                Timed_Text(
                    "Target has no Integer stacks!",
                    0.03,
                    True,
                    True
                )

        # Subtraction
        if AbilityType == 3:

            Self.Stamina -= 1

            Enemy_Choice = Choose_Enemy(Enemy1, Enemy2, Enemy3)

            if "Integer" in Enemy_Choice.Applied_Status:

                if Enemy_Choice.Applied_Status["Integer"] > 0:

                    Enemy_Choice.Applied_Status["Integer"] -= 1

                    Damage_Calc = Self.Strength - Enemy_Choice.Magic_Defense

                    if Damage_Calc < 0:
                        Damage_Calc = 0

                    Timed_Text(
                        f"{Self.Name} consumes an Integer stack "
                        f"from {Enemy_Choice.Name}!",
                        0.03,
                        True,
                        True
                    )

                    Enemy_Choice.Damage_Enemy(Damage_Calc)

                else:
                    Timed_Text(
                        "No Integer stacks available!",
                        0.03,
                        True,
                        True
                    )

        # Division
        if AbilityType == 4:

            Self.Stamina -= 1

            Enemy_Choice = Choose_Enemy(Enemy1, Enemy2, Enemy3)

            if "Integer" in Enemy_Choice.Applied_Status:

                Stacks = Enemy_Choice.Applied_Status["Integer"]

                if Stacks > 0:

                    Consume = max(1, Stacks // 2)

                    Enemy_Choice.Applied_Status["Integer"] -= Consume

                    Damage_Calc = (
                        Self.Strength * Consume
                    ) - Enemy_Choice.Magic_Defense

                    if Damage_Calc < 0:
                        Damage_Calc = 0

                    Timed_Text(
                        f"{Self.Name} divides reality itself!",
                        0.03,
                        True,
                        True
                    )

                    Timed_Text(
                        f"{Enemy_Choice.Name} takes "
                        f"-{Damage_Calc} damage!",
                        0.03,
                        True,
                        True
                    )

                    Enemy_Choice.Damage_Enemy(Damage_Calc)

    # =========================================================
    # ETERNAL SUFFERING : MAGE SUBCLASS
    # =========================================================

    if ClassType == "Eternal Suffering":

        # Earth's torment
        if AbilityType == 1:

            Self.Stamina -= 1

            for Enemy in Enemies:

                if "Magma" not in Enemy.Applied_Status:
                    Enemy.Applied_Status["Magma"] = 3

                Timed_Text(
                    f"Magma erupts beneath {Enemy.Name}!",
                    0.03,
                    True,
                    True
                )

        # Suffocation
        if AbilityType == 2:

            Self.Stamina -= 1

            Enemy_Choice = Choose_Enemy(Enemy1, Enemy2, Enemy3)

            Enemy_Choice.Magic_Defense -= int(Self.Strength / 2)

            Timed_Text(
                f"{Enemy_Choice.Name}'s magic resistance burns away!",
                0.03,
                True,
                True
            )

    # =========================================================
    # OUR LORD REINCARNATE. # MAG SUBCLASS
    # =========================================================

    if ClassType == "Our Lord reincarnate":

        # Cleanse
        if AbilityType == 1:

            Self.Stamina -= 1

            Self.Applied_Status.clear()

            Timed_Text(
                f"{Self.Name} cleanses all negative effects!",
                0.03,
                True,
                True
            )

        # God's left hand
        if AbilityType == 2:

            Self.Stamina -= 1

            for Enemy in Enemies:

                Damage_Calc = Self.Strength - Enemy.Magic_Defense

                if Damage_Calc < 0:
                    Damage_Calc = 0

                Timed_Text(
                    f"Holy light crashes into {Enemy.Name}!",
                    0.03,
                    True,
                    True
                )

                Enemy.Damage_Enemy(Damage_Calc)

    # =========================================================
    # TO IT'S ABSOLUTION
    # =========================================================

    if ClassType == "To it’s Absolution":

        if AbilityType == 1:

            Self.Stamina -= 1

            Self.Applied_Status["Aggression"] = 1

            Timed_Text(
                f"{Self.Name} braces against all attacks!",
                0.03,
                True,
                True
            )

        if AbilityType == 2:

            Self.Stamina -= 1

            Self.Applied_Status["Taunt"] = 1

            Timed_Text(
                f"All enemies are forced to target {Self.Name}!",
                0.03,
                True,
                True
            )

        if AbilityType == 3:

            Self.Stamina -= 1

            for Enemy in Enemies:

                Damage_Calc = Self.Strength - Enemy.Physical_Defense

                if Damage_Calc < 0:
                    Damage_Calc = 0

                Enemy.Damage_Enemy(Damage_Calc)

                Timed_Text(
                    f"{Self.Name} cuts through {Enemy.Name}!",
                    0.03,
                    True,
                    True
                )

    # =========================================================
    # SPECIES OF ANNIHILATION
    # =========================================================

    if ClassType == "Species of Annihilation":

        if AbilityType == 1:

            Self.Stamina -= 1

            Self.Health -= 10
            Self.Strength += Self.Strength

            Timed_Text(
                f"{Self.Name} sacrifices health for power!",
                0.03,
                True,
                True
            )

        if AbilityType == 2:

            Self.Stamina -= 1

            for Enemy in Enemies:

                Damage_Calc = Self.Strength - Enemy.Physical_Defense

                if Damage_Calc < 0:
                    Damage_Calc = 0

                Enemy.Damage_Enemy(Damage_Calc)

                Timed_Text(
                    f"{Enemy.Name} is eradicated for "
                    f"-{Damage_Calc} damage!",
                    0.03,
                    True,
                    True
                )

        if AbilityType == 3:

            Self.Stamina -= 1

            Enemy_Choice = Choose_Enemy(Enemy1, Enemy2, Enemy3)

            Enemy_Choice.Applied_Status["Execution"] = 1

            Damage_Calc = Self.Strength - Enemy_Choice.Physical_Defense

            if Damage_Calc < 0:
                Damage_Calc = 0

            Enemy_Choice.Damage_Enemy(Damage_Calc)

    # =========================================================
    # REPRISE OF THE VOID
    # =========================================================

    if ClassType == "Reprise of the void":

        if AbilityType == 1:

            Self.Stamina -= 1

            Enemy_Choice = Choose_Enemy(Enemy1, Enemy2, Enemy3)

            Enemy_Choice.Applied_Status["Silence"] = 1

            Damage_Calc = Self.Strength - Enemy_Choice.Physical_Defense

            if Damage_Calc < 0:
                Damage_Calc = 0

            Enemy_Choice.Damage_Enemy(Damage_Calc)

        if AbilityType == 2:

            Self.Stamina -= 1

            Self.Applied_Status["Invisible"] = 3

            Timed_Text(
                f"{Self.Name} fades into the void...",
                0.03,
                True,
                True
            )

        if AbilityType == 3:

            Self.Stamina -= 1

            for Enemy in Enemies:

                Enemy.Applied_Status["Silence"] = 3
                Enemy.Defence -= int(Self.Strength / 2)

    # =========================================================
    # DISSONANT COURAGE
    # =========================================================

    if ClassType == "Dissonant Courage":

        if AbilityType == 1:

            Self.Stamina -= 1

            Self.Applied_Status["TeamDamageBuff"] = Self.Strength

            Timed_Text(
                f"{Self.Name} inspires the entire team!",
                0.03,
                True,
                True
            )

        if AbilityType == 2:

            Self.Stamina -= 1

            Enemy_Choice = Choose_Enemy(Enemy1, Enemy2, Enemy3)

            Damage_Calc = Self.Strength - Enemy_Choice.Physical_Defense

            if Damage_Calc < 0:
                Damage_Calc = 0

            Enemy_Choice.Damage_Enemy(Damage_Calc)

        if AbilityType == 3:

            Self.Stamina -= 1

            Timed_Text(
                "An ally's cooldowns are refreshed!",
                0.03,
                True,
                True
            )

    # =========================================================
    # THE HOLY UNJUST
    # =========================================================

    if ClassType == "The Holy unjust":

        if AbilityType == 1:

            Self.Stamina -= 1

            for Enemy in Enemies:

                Damage_Calc = Self.Strength - Enemy.Magic_Defense

                if Damage_Calc < 0:
                    Damage_Calc = 0

                Enemy.Damage_Enemy(Damage_Calc)

        if AbilityType == 2:

            Self.Stamina -= 1

            Self.Applied_Status["Shield"] = Self.Strength

            Timed_Text(
                f"{Self.Name} spreads divine protection!",
                0.03,
                True,
                True
            )

        if AbilityType == 3:

            Self.Stamina -= 1

            Self.Health += Self.Strength

            Timed_Text(
                f"{Self.Name} is healed for "
                f"{Self.Strength} HP!",
                0.03,
                True,
                True
            )

    # =========================================================
    # UNWRITTEN MELODIES
    # =========================================================

    if ClassType == "Unwritten melodies":

        if AbilityType == 1:

            Self.Stamina -= 1

            Enemy_Choice = Choose_Enemy(Enemy1, Enemy2, Enemy3)

            Bonus = Self.Applied_Status.get("Stars", 0)

            Damage_Calc = (
                Self.Strength + Bonus
            ) - Enemy_Choice.Magic_Defense

            if Damage_Calc < 0:
                Damage_Calc = 0

            Enemy_Choice.Damage_Enemy(Damage_Calc)

            Timed_Text(
                f"A wishing star crashes into "
                f"{Enemy_Choice.Name}!",
                0.03,
                True,
                True
            )

        if AbilityType == 2:

            Self.Stamina -= 1

            if "Stars" not in Self.Applied_Status:
                Self.Applied_Status["Stars"] = 0

            Self.Applied_Status["Stars"] += Self.Strength

            Timed_Text(
                f"Stars gather around {Self.Name}...",
                0.03,
                True,
                True
            )

        if AbilityType == 3:

            Self.Stamina -= 1

            Timed_Text(
                "Wishing Star cooldown refreshed!",
                0.03,
                True,
                True
            )

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
        print(f"1: Addition: Summon an addition sign. dealing {Self.Strength} magic damage to a targeted enemy, applies a stack of Intiger.")
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
    
    


