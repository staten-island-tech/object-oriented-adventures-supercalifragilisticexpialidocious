import json, time, Reminderforhowtosavestufftojson

with open("./inventory.json", "r") as f:
    inventory = json.load(f) #weapons, pets, badges, armor
with open("./profile.json", "r") as f:
    profile = json.load(f) # profile is name, health, glowstones
usernames = open("./users.json", encoding="utf8")
user = json.load(usernames)
#write code here







with open("inventory.json", "w") as f:
    json_string = json.dumps(inventory, indent= 4)
    f.write(json_string)

with open("profile.json", "w") as f:
    json_string = json.dumps(profile, indent= 4)
    f.write(json_string)