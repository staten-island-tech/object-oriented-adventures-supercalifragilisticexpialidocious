import time, random
"""with open("./inventory.json", "r") as f:
    inventory = json.load(f) #weapons, pets, badges, armor
with open("./profile.json", "r") as f:
    profile = json.load(f) # profile is name, health, glowstones
usernames = open("./users.json", encoding="utf8")
user = json.load(usernames) """


""" def BattleDialogueTundra(): """
Energy = random.randint(10,15)


Enemy = "Arctic Fox"
EnemyHealth = 100
playerhealth = 100
umbrella = 20


print(f"You have encountered a {Enemy}!")
print(f"You have {Energy} Energy")
choice = input("[1] > Fight\n[2] > Run away\n> ")
if choice == "1":
    print(f"{Enemy} dealt 10 damage")
    playerhealth = playerhealth - 10
    fight = input("[1] > Use your weapon, -5 Energy\n[2] > Punch, -2 energy\n[3] > Kick, -2 energy\n> ")
    if fight == 1:
        print(f"You dealt {umbrella} damage")
        EnemyHealth -= umbrella
        Energy -= 5
    elif fight == 2:
        print("You dealt 5 damage")
        EnemyHealth = EnemyHealth - 5
        Energy = Energy - 2
    elif fight == 3:
        print("You dealt 5 damage")
        EnemyHealth - 5
        Energy = Energy - 2
    
print(playerhealth)
print(EnemyHealth)
print(Energy)





#ADHD npc dialogue:

""" def ADHDNPC():
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
        print("ok kys") """


""" 
with open("inventory.json", "w") as f:
    json_string = json.dumps(inventory, indent= 4)
    f.write(json_string)

with open("profile.json", "w") as f:
    json_string = json.dumps(profile, indent= 4)
    f.write(json_string) """