import random, json, os
promocode = open("./promocode.json", encoding="utf8")
data = json.load(promocode)
glow = open("./glowstones.json", encoding="utf8")
glowstone = json.load(glow)
glowstones = glowstone["glowstones"]

class Usefulbots:
    def WenQian():
        print("Hello my name is Wen Qian!")
        print("Wen Qian: What do you need help with?")
        question = input("[1] > Bring me to weapon gacha\n[2] > Bring me to gear gacha\n[3] > Bring me to pet gacha\n[4] > Buy gacha tickets\n[5] > See rarities\n[6] >  Enter promocode")
    def Sarah():
        print("Hello, I am Sarah!")
        print("Sarah: What do you need help with?")
        question = input("[1] > View your quests\n[2] > How do I gain badges?\n[3] > Where do you find weapons and gears?\n[4] > How do I level up?\n[5] Enter promocode\n> ")
        if question == "1":
            print("Here are your quests:")
        elif question == "2":
            print("You gain badges by encountering secrets, completing specific quests, obtaining collectables, and entering promocodes.")
        elif question == "3":
            print("You can find weapons and gears by going to Wen Qian's shop and buying a ticket.")
        elif question == "4":
            print("You can level up by completing quests and fighting monsters.")
        elif question == "5":
            promo = input("Type in the promocode:\n> ")
            for code in data:
                if code["promocode"] == promo:
                    print("You have just gained 100 exp and a badge!")
                    glowstones.append(100)
                elif promo not in code["promocode"]:
                    print("That is not a promocode")

Usefulbots.Sarah()

