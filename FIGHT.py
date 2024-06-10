import random, json, time, os

class Game:
    def __init__(self):
        self.player_hp = 200
        self.player_attack = 20
        self.inventory_file_path = "Inventory.json"

    def load_inventory(self):
        with open(self.inventory_file_path, 'r') as file:
            return json.load(file)

    def update_inventory(self, glowstones):
        inventory = self.load_inventory()
        inventory['Glowstones'] += glowstones
        with open(self.inventory_file_path, 'w') as file:
            json.dump(inventory, file)

    class Fight:
        def __init__(self, player_hp, player_attack, inventory_file_path):
            self.player_hp = player_hp
            self.player_attack = player_attack
            self.inventory_file_path = inventory_file_path
            self.encounters = [
                {"Name": "Arctic Fox", "Hp": 100, "Attack": 10, "Glowstones": 50},
                {"Name": "Snow Leopard", "Hp": 100, "Attack": 10, "Glowstones": 50},
                {"Name": "Polar Bear", "Hp": 100, "Attack": 10, "Glowstones": 50},
                {"Name": "Elk", "Hp": 100, "Attack": 10, "Glowstones": 50},
                {"Name": "Eagle", "Hp": 100, "Attack": 10, "Glowstones": 50},
                {"Name": "Salamander", "Hp": 200, "Attack": 20, "Glowstones": 100},
                {"Name": "Lizard", "Hp": 200, "Attack": 20, "Glowstones": 100},
                {"Name": "Deer", "Hp": 200, "Attack": 20, "Glowstones": 100},
                {"Name": "Owl", "Hp": 200, "Attack": 20, "Glowstones": 100},
                {"Name": "Wolf", "Hp": 200, "Attack": 20, "Glowstones": 100},
                {"Name": "Mothman", "Hp": 200, "Attack": 20, "Glowstones": 100},
                {"Name": "Zebra", "Hp": 300, "Attack": 40, "Glowstones": 200},
                {"Name": "Cobra", "Hp": 300, "Attack": 40, "Glowstones": 200},
                {"Name": "Ferret", "Hp": 300, "Attack": 40, "Glowstones": 200},
                {"Name": "Hyena", "Hp": 300, "Attack": 40, "Glowstones": 200},
                {"Name": "Cheetah", "Hp": 300, "Attack": 40, "Glowstones": 200},
                {"Name": "Basilisk", "Hp": 300, "Attack": 40, "Glowstones": 200},
                {"Name": "Chimera", "Hp": 400, "Attack": 60, "Glowstones": 300},
                {"Name": "Nymph", "Hp": 400, "Attack": 60, "Glowstones": 300},
                {"Name": "Goldhorn", "Hp": 400, "Attack": 60, "Glowstones": 300},
                {"Name": "Giant Hawk", "Hp": 400, "Attack": 60, "Glowstones": 300},
                {"Name": "Gargoyle", "Hp": 400, "Attack": 60, "Glowstones": 300},
                {"Name": "Giant Leaf Dragon", "Hp": 800, "Attack": 50, "Glowstones": 1000},
                {"Name": "Charybdis", "Hp": 500, "Attack": 80, "Glowstones": 500},
                {"Name": "Leviathan", "Hp": 500, "Attack": 80, "Glowstones": 500},
                {"Name": "Kraken", "Hp": 500, "Attack": 80, "Glowstones": 500},
                {"Name": "Hydra", "Hp": 500, "Attack": 80, "Glowstones": 500},
                {"Name": "Capricorn", "Hp": 500, "Attack": 80, "Glowstones": 500}
            ]

        def fight_sequence(self):
            os.system('cls')
            encounter = random.choice(self.encounters)
            print(f"Encounter: {encounter['Name']}")
            print(f"Enemy HP: {encounter['Hp']}")
            print(f"Enemy Attack: {encounter['Attack']}")
            time.sleep(1)

            while self.player_hp > 0 and encounter['Hp'] > 0:
                print("\nYour Turn:")
                print(f"Player HP: {self.player_hp}")
                print(f"Player Attack: {self.player_attack}")

                action = input("Enter 'A' to attack or 'R' to run: ").upper()

                if action == 'A':
                    os.system('cls')
                    print("You have attacked!")
                    if random.randint(1, 4) == 1:
                        encounter['Hp'] -= 60
                        print("Critical Hit!")
                    else:
                        encounter['Hp'] -= self.player_attack
                    print(f"{encounter['Name']} HP: {encounter['Hp']}")

                elif action == 'R':
                    print("Bro ran away!")
                    return 0

                else:
                    print("Please enter 'A' to attack or 'R' to run.")
                    time.sleep(1)
                    os.system('cls')

                if encounter['Hp'] > 0:
                    print("\nEnemy Turn:")
                    print("Enemy attacks!")
                    self.player_hp -= encounter['Attack']
                    print(f"Player HP: {self.player_hp}")

                    if self.player_hp <= 0:
                        self.player_hp = 0
                        print(f"\nYou were killed by {encounter['Name']}...")
                        return -1

    def start_fight(self):
        fight_instance = self.Fight(self.player_hp, self.player_attack, self.inventory_file_path)
        glowstones_earned = fight_instance.fight_sequence()

        if glowstones_earned > 0:
            self.update_inventory(glowstones_earned)
            print(f"You gained {glowstones_earned} glowstones.")
