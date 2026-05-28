from Systems.Functions import Timed_Text
from Systems.Class import ClassDescript
from Systems.Class import Class_Ability_Description
from Systems.Class import Class_Ability_Cast


class Units:

    def __init__(self, Name, Class):

        self.Name = Name
        self.MaxHealth = 10
        self.Health = 10
        self.Strength = 2
        self.Defence = 0
        self.Physical_Defense = 0
        self.Magic_Defense = 0
        self.Dodge = 10
        self.Dash = 1
        self.MaxStamina = 2
        self.Stamina = 2
        self.Relationship_Status = 1
        self.Relationshp_Level = 1
        self.Class = Class
        self.Equipement = 0

        self.Applied_Status = {}

        self.Class_Passive()

    def ClassDescript(Self):
        x = ClassDescript(Self)
        return x

    def Class_Passive(Self):
        Class = ClassDescript(Self)
        if Class == "Hunter":
            Self.Dodge += 25
            Self.MaxStamina = 3
            Self.Stamina = 3

    # STATUS ENDINGS / ROUND TICK

    def Status_Ending(Self):
        Remove_List = []
        
        # WARRIOR BLOCK
        if "WarriorAbility2" in Self.Applied_Status:
            if Self.Applied_Status["WarriorAbility2"] <= 0:
                Remove_List.append("WarriorAbility2")
                Self.Defence -= 2
                Timed_Text(
                    f"{Self.Name}'s Block fades.",
                    0.03,
                    True,
                    True
                )
            else:
                Self.Applied_Status["WarriorAbility2"] -= 1
                
        # MAGMA
        if "Magma" in Self.Applied_Status:
            Damage = 2
            Self.Take_Damage(Damage)
            Timed_Text(
                f"{Self.Name} burns in magma for "
                f"-{Damage} damage!",
                0.03,
                True,
                True
            )
            Self.Applied_Status["Magma"] -= 1
            if Self.Applied_Status["Magma"] <= 0:
                Remove_List.append("Magma")
                Timed_Text(
                    f"The magma beneath {Self.Name} cools.",
                    0.03,
                    True,
                    True
                )

        # INVISIBLE
        if "Invisible" in Self.Applied_Status:
            Self.Applied_Status["Invisible"] -= 1
            if Self.Applied_Status["Invisible"] <= 0:
                Remove_List.append("Invisible")
                Timed_Text(
                    f"{Self.Name} becomes visible again.",
                    0.03,
                    True,
                    True
                )

        # SILENCE
        if "Silence" in Self.Applied_Status:
            Self.Applied_Status["Silence"] -= 1
            if Self.Applied_Status["Silence"] <= 0:
                Remove_List.append("Silence")
                Timed_Text(
                    f"{Self.Name} can use abilities again.",
                    0.03,
                    True,
                    True
                )

        # AGGRESSION
        if "Aggression" in Self.Applied_Status:
            Self.Applied_Status["Aggression"] -= 1
            if Self.Applied_Status["Aggression"] <= 0:
                Remove_List.append("Aggression")
                Timed_Text(
                    f"{Self.Name}'s aggression fades.",
                    0.03,
                    True,
                    True
                )

        # TAUNT
        if "Taunt" in Self.Applied_Status:
            Self.Applied_Status["Taunt"] -= 1
            if Self.Applied_Status["Taunt"] <= 0:
                Remove_List.append("Taunt")
                Timed_Text(
                    f"Enemies stop focusing {Self.Name}.",
                    0.03,
                    True,
                    True
                )

		# EXECUTION MARK

        if "Execution" in Self.Applied_Status:
            Self.Applied_Status["Execution"] -= 1
            if Self.Applied_Status["Execution"] <= 0:
                Remove_List.append("Execution")
                Timed_Text(
                    f"{Self.Name}'s execution mark fades.",
                    0.03,
                    True,
                    True
                )

        # SHIELD

        if "Shield" in Self.Applied_Status:
            if Self.Applied_Status["Shield"] <= 0:
                Remove_List.append("Shield")
                Timed_Text(
                    f"{Self.Name}'s shield breaks.",
                    0.03,
                    True,
                    True
                )

        # REMOVE EXPIRED STATUSES

        for Status in Remove_List:
            if Status in Self.Applied_Status:
                del Self.Applied_Status[Status]

    # DEATH CHECK

    def IsDied(self):
        if self.Health <= 0:
            return True
        return False

    # TAKE DAMAGE

    def Take_Damage(self, Amount):
        if self.Health <= 0:
            return
        # DASH
        
        if self.Dash > 0:
            self.Success_Dash()
            return

        # INVISIBLE

        if "Invisible" in self.Applied_Status:
            Timed_Text(
                f"{self.Name} avoids the attack while invisible!",
                0.03,
                True,
                True
            )
            return

        # AGGRESSION DAMAGE REDUCTION

        if "Aggression" in self.Applied_Status:
            Amount = int(Amount * 0.25)

        # SHIELD

        if "Shield" in self.Applied_Status:
            ShieldValue = self.Applied_Status["Shield"]
            if ShieldValue >= Amount:
                self.Applied_Status["Shield"] -= Amount
                Timed_Text(
                    f"{self.Name}'s shield absorbs the damage!",
                    0.03,
                    True,
                    True
                )
                return
            else:
            	Amount -= ShieldValue
                self.Applied_Status["Shield"] = 0
                Timed_Text(
                    f"{self.Name}'s shield shatters!",
                    0.03,
                    True,
                    True
                )

        # DEFENCE

        Amount -= self.Defence

        if Amount < 0:
            Amount = 0

        # FINAL DAMAGE
        self.Health -= Amount

        Timed_Text(
            f"{self.Name} takes -{Amount} damage!",
            0.03,
            True,
            True
        )

        if self.Health < 0:
            self.Health = 0

    # DASH SUCCESS

    def Success_Dash(self):
        self.Dash -= 1
        Timed_Text(
            "Missed damage!",
            0.03,
            True,
            True
        )

    # ACTION

    def Action(Self, Enemy1, Enemy2, Enemy3):
        # Silence check
    	if "Silence" in Self.Applied_Status:
            Timed_Text(
                f"{Self.Name} is silenced and cannot cast abilities!",
                0.03,
                True,
                True
            )
            return

        # No stamina

        if Self.Stamina <= 0:
            Timed_Text(
                f"{Self.Name} is too exhausted!",
                0.03,
                True,
                True
            )
            return
        Timed_Text(
            "Select an action!",
            0.03,
            True,
            False
        )
        print(Self.Name, " ", end="")
        print("(", ClassDescript(Self), ")", sep="")
        ChoseAbility = Class_Ability_Description(Self)
        Class_Ability_Cast(
            Self,
            ChoseAbility,
            Enemy1,
            Enemy2,
            Enemy3
        )

    # TURN RESET

    def Turn_Reset(Self):
        Self.Stamina = Self.MaxStamina
        if Self.Dash < 0:
            Self.Dash = 0

    # DISPLAY INFO
    def Display_Stats(Self):

        print("-------------------------------")
        print(f"Name: {Self.Name}")
        print(f"Class: {ClassDescript(Self)}")
        print(f"HP: {Self.Health}/{Self.MaxHealth}")
        print(f"Stamina: {Self.Stamina}/{Self.MaxStamina}")
        print(f"Strength: {Self.Strength}")
        print(f"Defence: {Self.Defence}")
        print(f"Dodge: {Self.Dodge}%")

        if len(Self.Applied_Status) > 0:
            print("Statuses:")
            for Status in Self.Applied_Status:
                print(
                    f"- {Status}: "
                    f"{Self.Applied_Status[Status]}"
                )

        print("----------------------------")