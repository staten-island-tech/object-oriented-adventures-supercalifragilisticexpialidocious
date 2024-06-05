import json
import random

with open('Additional/Encounters.json', 'r') as file:
    enemy_data = json.load(file)

print("Enemy Data:", enemy_data)

def fight(player_level, realm):
    enemies = [enemy for enemy in enemy_data if enemy['Realm'] == realm]
    
    if not enemies:
        print("Erm what the sigma")
        return None
    
    enemy = random.choice(enemies)
    
    print(f"You encountered a {enemy['Name']}!")
    player_hp = 100
    enemy_hp = enemy['Hp']
    
    while player_hp > 0 and enemy_hp > 0:
        enemy_hp -= random.randint(15, 20)
        print(f"Enemy HP: {enemy_hp}")
        if enemy_hp <= 0:
            print("You win WHOOOPEEE!")
            return enemy['Glowstones']
        
        player_hp -= enemy['Attack']
        print(f"Enemy attacks! Player HP: {player_hp}")
        if player_hp <= 0:
            print("L bro died haha! bros deathmaxxing")
            return 0

player_level = 23
realm = "Jungle City"  

print(f"Player level: {player_level}, Realm: {realm}")

glowstones_earned = fight(player_level, realm)
if glowstones_earned is not None:
    print(f"Glowstones earned: {glowstones_earned}")
