import random, time, json
poke = open("./Gacha.json", encoding="utf8")
weapon = json.load(poke)


class Weapon:
    def Gacha():
        x = float(input("Input seconds delay following script:\n>"))
        def sleep(x):
            time.sleep(x)
        print("Welcome to the Weapon Gacha!")
        sleep(x)
        p = input("What would you like to do?\n[1] > Use your gacha ticket\n[2] > Exit\n>  ")
        if p == "1":
            x = random.randint(1,3750)
            if x == [1,2,3,4,5]:
                d = random.randint(1,2)
                if d == 1:
                    print("You just obtained Valhalla Staff!")
                elif d == 2:
                    print(" You ahve just obtained Pyrium Staff!")
            elif x > 5 and x < 196:
                c = random.randint(1,3)
    
