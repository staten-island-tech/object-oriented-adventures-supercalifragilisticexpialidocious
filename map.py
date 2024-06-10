import random, os, json, time
from GachaSystem import GachaSystem

class GameThing:
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
        def __init__(self, player_hp, player_attack, inventory_file_path, encounters):
            self.player_hp = player_hp
            self.player_attack = player_attack
            self.inventory_file_path = inventory_file_path
            self.encounters = encounters

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
                    print("You ran away!")
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
        encounters =  [
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
        fight_instance = self.Fight(self.player_hp, self.player_attack, self.inventory_file_path, encounters)
        glowstones_earned = fight_instance.fight_sequence()

        if glowstones_earned > 0:
            self.update_inventory(glowstones_earned)
            print(f"You gained {glowstones_earned} glowstones.")

class NPC:
    def __init__(self):
        self.interact()

    def interact(self):
        x = random.randint(1,10)
        if x == 1:
            input("Barney: Why can't dinosaurs clap??\n> ")
            print("Barney: Because they're dead. AHAHAHAHAHAHAH")
        elif x == 2:
            print("Wen Qian: Donate me robux at 1886i PLS PLS PLS PLS PLS PLS")
        elif x == 3:
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
                print("ok die")
        elif x == 4:
            r = input("Sarah: Am I awesome sauce? Y|N\n> ")
            if r.lower() == "y":
                print("Sarah: Yay thanks! You're also awesome sauce")
            elif r.lower() == "n":
                print("Sarah: You're stinky")
        elif x == 5:
            print("Skobodo Urino: Pod pod pod no no")
        elif x == 6:
            print("Whalen: I am apart of the asian community because how would I know Fei Long if I wasn't?")
        elif x == 7:
            print("JeffBoy_123: In mathematics, the Riemann hypothesis is the conjecture that the Riemann zeta function has its zeros only at the negative even integers and complex numbers with real part 1/2. Many consider it to be the most important unsolved problem in pure mathematics.[1] It is of great interest in number theory because it implies results about the distribution of prime numbers. It was proposed by Bernhard Riemann (1859), after whom it is named. The Riemann hypothesis and some of its generalizations, along with Goldbach's conjecture and the twin prime conjecture, make up Hilbert's eighth problem in David Hilbert's list of twenty-three unsolved problems; it is also one of the Clay Mathematics Institute's Millennium Prize Problems, which offers US$1 million to anyone who solves any of them. The name is also used for some closely related analogues, such as the Riemann hypothesis for curves over finite fields. The Riemann zeta function ζ(s) is a function whose argument s may be any complex number other than 1, and whose values are also complex. It has zeros at the negative even integers; that is, ζ(s) = 0 when s is one of -2, -4, -6, .... These are called its trivial zeros. The zeta function is also zero for other values of s, which are called nontrivial zeros. The Riemann hypothesis is concerned with the locations of these nontrivial zeros, and states that: The real part of every nontrivial zero of the Riemann zeta function is 1/2. Thus, if the hypothesis is correct, all the nontrivial zeros lie on the critical line consisting of the complex numbers 1/2 + it, where t is a real number and i is the imaginary unit.")
        elif x == 8:
            f = input("Davinki: Hai wanna be apart of my newest drawing? (I have come back from the dead) Y|N\n> ")
            if f.lower() == "y":
                print("Davinki: Actually, after further inspection, no thanks!")
            elif f.lower() == "n":
                print("Davinki: Whatever, you weren't cut out to model anyway")
        elif x == 9:
            print("Drake: Kendrick is NOT skboodo urino.")
        elif x == 10:
            print("Kendrick: Drake is a MEANIE WEANIE")

class Maps:
    @staticmethod
    def map(setting, setting2, setting3, glowstones, NPCS, enemies):
        GachaSystem.NPC().interact()

        playerCoords = [0, 1]
        mapSize = [40, 100]
        def clear(): os.system("cls")
        map_grid = [['|' if i in [0] else '  ' for i in range(100)] for _ in range(40)]
        for row in map_grid: 
            for i in range(2):
                row[random.randint(1, 98)] = f'{setting}' 
                if random.randint(1, 5) == 1:
                    row[random.randint(1, 98)] = f"{setting2}"
                if random.randint(1, 10) == 1:
                    row[random.randint(1, 98)] = f"{setting3}"
                if random.randint(1, 10) == 1:
                    row[random.randint(1, 98)] = f"{glowstones}"
                if random.randint(1, 10) == 1:
                    row[random.randint(1, 98)] = f"{NPCS}"
                if random.randint(1, 13) == 1:
                    row[random.randint(1, 98)] = f"{enemies}"
        map_grid[playerCoords[0]][playerCoords[1]] = "🟥"

        def load_data():
            with open('Inventory.json', 'r') as f:
                return json.load(f)
        
        def save_data(data):
            with open('Inventory.json', 'w') as f:
                json.dump(data, f, indent=4)

        def print_map(): 
            for row in map_grid: 
                print(''.join(row))

        while True: 
            clear()
            print_map()
            whereToGo = input("W/A/S/D to move: ").upper()
            nextCoords = list(playerCoords)
            if whereToGo == "W" and nextCoords[0] - 1 >= 0:
                nextCoords[0] -= 1
            elif whereToGo == "A":
                nextCoords[1] -= 1
            elif whereToGo == "S" and nextCoords[0] + 1 < mapSize[0]:
                nextCoords[0] += 1
            elif whereToGo == "D" and nextCoords[1] + 1 < mapSize[1]:
                nextCoords[1] += 1
            elif whereToGo == "E":
                os.system('cls')
                GachaSystem.NPC().interact()
                nextCoords[1] += 1

            nextCell = map_grid[nextCoords[0]][nextCoords[1]]
            if nextCell not in ["|", f"{setting}", f"{setting2}", f"{setting3}"]:
                map_grid[playerCoords[0]][playerCoords[1]] = "  "
                playerCoords = list(nextCoords)
                map_grid[playerCoords[0]][playerCoords[1]] = "🟥"
            if nextCell == f'{glowstones}':
                data = load_data()
                data["Glowstones"] += 250
                save_data(data)
            elif nextCell == f'{NPCS}':
                os.system('cls')
                npc = NPC()
                npc.interact()
            elif nextCell == f'{enemies}':
                os.system('cls')
                game_instance = GameThing()
                game_instance.start_fight()
