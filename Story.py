import json, time
"""with open("./inventory.json", "r") as f:
    inventory = json.load(f) #weapons, pets, badges, armor
with open("./profile.json", "r") as f:
    profile = json.load(f) # profile is name, health, glowstones
usernames = open("./users.json", encoding="utf8")
user = json.load(usernames) """


""" #Battle dialogue:
print(f"You have encountered a !")
choice = input("[1] > Fight\n[2] > Run away\n> ")
 """


#ADHD npc dialogue:
print("Knock Knock")
o = input("[1] > Who's there?\n[2] > Go away hippie\n> ")
if o == "1":
    input("Hatch\n> ")
    print("Bless you! AH HA")
    time.sleep(.7)
    print("AH HA.")
    time.sleep(.7)
    print("AH HA.")
elif o == "2":
    print("ok kys")


""" 
with open("inventory.json", "w") as f:
    json_string = json.dumps(inventory, indent= 4)
    f.write(json_string)

with open("profile.json", "w") as f:
    json_string = json.dumps(profile, indent= 4)
    f.write(json_string) """