class Enemy:
    def __init__(self,Type):
        self.Type = Type
        Self.Name = "Enemy"
        self.Strength = 1
        self.MaxHealth = 1
        self.Dodge = 10 ### 10% dodge chance
        self.Dash = 0 # 1 = it will block.Dash 1 Damage.
        self.Health = 1 ## Howmuch units have fallen!
        self.Dash = 0 ## 1 count Used on hit
        self.Dodge = 0 ## 0%
        
        self.Magic_Defense = 0
        self.Physical_Defense = 0
        if Type == 1:
            Self.Name = "Enemy1"
            self.Strength = 1
            self.MaxHealth = 2
            self.Health = 2
        elif Type == 2:
            Self.Name = "Enemy2"
            self.Strength = 2
            self.MaxHealth = 3
            self.Health = 3

    def Heal_Enemy(self,Amunt):
        if Self.MaxHealth > Self.Health:
            self.Health += amount
        else:
            Self.Health = Self.MaxHealth
    def Damage_Enemy(self, amount):
        if Self.MaxHealth > Self.Health:
            self.Health -= amount
        else:
            Self.Health = Self.MaxHealth
        
    def IsDied(self):
        if self.Health <= 0:
            return True
