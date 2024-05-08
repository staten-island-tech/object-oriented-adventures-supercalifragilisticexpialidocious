import json
import os
## Create Class for creating new dictionaries here
menu = input("What do you want to do? \n(1) Add item to the dictionary ")

with open("Encounters.json", "r") as f:
    data = json.load(f)

class Entitty:
    def createPokemon(self):
        realm = input("What realm is it? \n>")
        lvlreq = input("What lvl does it require?\n>")
        enemy = input("Enemies?\n>")
        while enemy.upper() == "Y":
            name = input("What is the enitity's name? \n>")
            attack = input("How much damage does the entity's attack do? \n>")
            glow = input("How much glowstones does it drop?\n>")
            hp = input("what hp is the enitty\n>")
            enemy = input("More?\n>")
        else:
            pass

        Realms = {
            "Realm" : realm,
            "LevelReq" : lvlreq,
            "Enemies" : [
                {"Name": name.capitalize(),
                "Hp": int(hp),
                "Attack": int(attack),
                "Glowstones": int(glow)
                }
            ]
        }
        data.append(Realms)


p = Entitty()

       
while menu == "1":
     p.createPokemon()
"""      o = input("Do you want to add another pokemon? Y|N\n>")
     if o.upper() == "N" :
         break """



""" new_file = "updated.json" """
with open("Encounters.json", "w") as f:
    json_string = json.dumps(data, indent= 4)
    f.write(json_string)
    
""" os.remove("data.json")
os.rename(new_file, "data.json") """
# Overwrite the old JSON file with the new one