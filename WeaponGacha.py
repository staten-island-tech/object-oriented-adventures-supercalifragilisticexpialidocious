import random, time, json
poke = open("./weapon.json", encoding="utf8")
weapon = json.load(poke)

def find(list, target):
    return next((i for i, item in enumerate(list) if item["WeaponName"] == target))


class Weapon:
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
                    t = weapon[find(weapon, "Valhalla Staff")]
                    with open("Inventory.json", "w") as inventory:
                        json.dump(t, inventory)
                elif d == 2:
                    print("You just obtained a Pyrium Staff!")
                    t = weapon[find(weapon, "Pyrium Staff")]
                    with open("Inventory.json", "w") as inventory:
                        json.dump(t, inventory)
            """ elif x > 5 and x < 196:
                c = random.randint(1,3)
                if c == 1:
                    print("You just obtained a Onyx Staff!")
                elif c == 2:
                    print("You just obtained a Trident!")
                elif c ==3:
                    print("You just obtained a S'mores Wand!")
            elif x > 195 and x <551:
                f = random.randint(1,2)
                if f == 1:
                    print("You just obtained a BIGG WATERMELON!")
                elif f == 2:
                    print("You just obtained a Sun Shield!")
            elif x > 550 and x < 1001:
                d = random.randint(1,5)
                if d == 1:
                    print("You just obtained a Draconyx!")
                elif d ==2:
                    print("You just obtained a Pheonix Talon!")
                elif d ==3:
                    print("You just obtained a Mechano Mace!")
                elif d ==4:
                    print("You just obtained a Moon wand!")
                elif d ==5:
                    print("You just obtained a Thunderbuster!")
            elif x > 1000 and x < 1751:
                r = random.randint(1,5)
                if r == 1:
                    print("You just obtained a Dual Blade!")
                elif r ==2:
                    print("You just obtained a Frosted Spear!")
                elif r ==3:
                    print("You just obtained a Flame Staff!")
                elif r ==4:
                    print("You just obtained a Raider's Staff!")
                elif r ==5:
                    print("You just obtained a Plasma Drill!")
            elif x > 1750 and x < 2751:
                t = random.randint(1,5)
                if t == 1:
                    print("You just obtained a Energy Staff!")
                elif t ==2:
                    print("You just obtained a Rock Guitar!")
                elif t ==3:
                    print("You just obtained a Big Scissors!")
                elif t ==4:
                    print("You just obtained a Poke Fork!")
                elif t ==5:
                    print("You just obtained a Hockey Stick!")
            elif x > 2750 and x < 3751:
                f = random.randint(1,5)
                if f == 1:
                    print("You just obtained a Umbrella!")
                elif f ==2:
                    print("You just obtained a Long Fungus!")
                elif f ==3:
                    print("You just obtained a Hammer!")
                elif f ==4:
                    print("You just obtained a Pencil!")
                elif f ==5:
                    print("You just obtained a Selfie stick!")
        elif p == 2:
            pass
 """

Weapon.Gacha()