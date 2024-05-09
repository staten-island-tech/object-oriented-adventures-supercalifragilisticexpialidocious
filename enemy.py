class Enemy():
    def __init__(self, name, hp, attack, glowstones):
        super().__init__()
        self.name = name
        self.hp = hp
        self.attack = attack
        self.glowstones = glowstones


ArcticFox = Enemy("ArcticFox", 100, 10, 50)
SnowLeopard = Enemy("ArcticFox", 100, 10, 50)
PolarBear = Enemy("ArcticFox", 100, 10, 50)
Elk = Enemy("ArcticFox", 100, 10, 50)
Eagle = Enemy("ArcticFox", 100, 10, 50)
Bob = Enemy("ArcticFox", 100, 10, 50)