import os, random, time, json
x = open("./weapon.json", encoding="utf8")
y = json.load(x)

class Encounter:
    def find(name):
        for type in y:
            if name == type['Name']:
                print(type)
                with open('Encounters.json' , 'r+') as f:
                    d = json.load(f)
                    d.append(type)
                    json.dump(d, f, indent = 4)