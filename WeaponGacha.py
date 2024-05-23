import random, time, json
poke = open("./weapon.json", encoding="utf8")
weapon = json.load(poke)


class Weapon:
    def find(name):
        for type in weapon:
            if name == type['WeaponName']:
                print(type)
                with open('Inventory.json' , 'r+') as f:
                    d = json.load(f)
                    d.append(type)
                    f.seek(0)
                    json.dump(d, f, indent = 4)
    
            
    def Gacha():
        x = float(input("Input seconds delay following script:\n>"))
        def sleep(x):
            time.sleep(x)
        print("Welcome to the Weapon Gacha!")
        sleep(x)
        p = input("What would you like to do?\n[1] > Use your gacha ticket\n[2] > Exit\n>  ")
        if p == "1":
            x = random.randint(1,5)
            if x > 0 and x < 6:
                d = random.randint(1,2)
                if d == 1:
                    print("You just obtained a Valhalla Staff!")
                    Weapon.find("Valhalla Staff")
                elif d == 2:
                    print("You just obtained a Pyrium Staff!")
                    Weapon.find("Pyrium Staff")
                    
            elif x > 5 and x < 196:
                c = random.randint(1,3)
                if c == 1:
                    print("You just obtained a Onyx Staff!")
                    Weapon.find("Onyx Staff")
                elif c == 2:
                    print("You just obtained a Trident!")
                    Weapon.find("Trident")
                elif c ==3:
                    print("You just obtained a S'mores Wand!")
                    Weapon.find("S'mores Wand")
            elif x > 195 and x <551:
                f = random.randint(1,2)
                if f == 1:
                    print("You just obtained a BIGG WATERMELON!")
                    Weapon.find("BIGG WATERMELON")
                elif f == 2:
                    print("You just obtained a Sun Shield!")
                    Weapon.find("Sun Shield")
            elif x > 550 and x < 1001:
                d = random.randint(1,5)
                if d == 1:
                    print("You just obtained a Draconyx!")
                    Weapon.find("Draconyx")
                elif d ==2:
                    print("You just obtained a Pheonix Talon!")
                    Weapon.find("Pheonix Talon")
                elif d ==3:
                    print("You just obtained a Mechano Mace!")
                    Weapon.find("Mechano Mace")
                elif d ==4:
                    print("You just obtained a Moon Wand!")
                    Weapon.find("Moon Wand")
                elif d ==5:
                    print("You just obtained a Thunderbuster!")
                    Weapon.find("Thunderbuster")
            elif x > 1000 and x < 1751:
                r = random.randint(1,5)
                if r == 1:
                    print("You just obtained a Dual Blade!")
                    Weapon.find("Dual Blade")
                elif r ==2:
                    print("You just obtained a Frosted Spear!")
                    Weapon.find("Frosted Spear")
                elif r ==3:
                    print("You just obtained a Flame Staff!")
                    Weapon.find("Flame Staff")
                elif r ==4:
                    print("You just obtained a Raider's Staff!")
                    Weapon.find("Raider's Staff")
                elif r ==5:
                    print("You just obtained a Plasma Drill!")
                    Weapon.find("Plasma Drill")
            elif x > 1750 and x < 2751:
                t = random.randint(1,5)
                if t == 1:
                    print("You just obtained a Energy Staff!")
                    Weapon.find("Energy Staff")
                elif t ==2:
                    print("You just obtained a Rock Guitar!")
                    Weapon.find("Rock Guitar")
                elif t ==3:
                    print("You just obtained a Big Scissors!")
                    Weapon.find("Big Scissors")
                elif t ==4:
                    print("You just obtained a Poke Fork!")
                    Weapon.find("Poke Fork")
                elif t ==5:
                    print("You just obtained a Hockey Stick!")
                    Weapon.find("Hockey Stick")
            elif x > 2750 and x < 3751:
                f = random.randint(1,5)
                if f == 1:
                    print("You just obtained a Umbrella!")
                    Weapon.find("Umbrella")
                elif f ==2:
                    print("You just obtained a Long Fungus!")
                    Weapon.find("Long Fungus")
                elif f ==3:
                    print("You just obtained a Hammer!")
                    Weapon.find("Hammer")
                elif f ==4:
                    print("You just obtained a Pencil!")
                    Weapon.find("Pencil")
                elif f ==5:
                    print("You just obtained a Selfie stick!")
                    Weapon.find("Selfie Stick")
        elif p == 2:
            pass


Weapon.Gacha()