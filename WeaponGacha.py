import random, json, os, time

class WeaponGacha:
    def anim(text, delay=0.02):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def __init__(self):
        with open("Weapons.json", encoding="utf8") as file:
            self.weapons_data = json.load(file)

        self.drop_rates = {
            "???": 0.05,
            "Mythical": 1.95,
            "Legendary": 5.5,
            "Ultra": 10,
            "Epic": 17.5,
            "Rare": 27.5,
            "Common": 37.5
        }

    def add_item_to_inventory(self, item):
        with open("Inventory.json", "r") as file:
            inventory = json.load(file)

        if 'Weapons' not in inventory:
            inventory['Weapons'] = []
        if item in inventory['Weapons']:
            os.system('cls')
            WeaponGacha.anim("You already have this item, so you get +750 Glowstones instead!")
            inventory['Glowstones'] = inventory.get('Glowstones', 0) + 750
        else:
            inventory['Weapons'].append(item)

        with open("Inventory.json", "w") as file:
            json.dump(inventory, file, indent=4)

    def gacha(self):
        if self.check_gacha_ticket():
            self.use_gacha_ticket()
            random_number = random.uniform(0, 100)
            cumulative_probability = 0
            selected_rarity = None

            for rarity, probability in self.drop_rates.items():
                cumulative_probability += probability

                if random_number <= cumulative_probability:
                    selected_rarity = rarity
                    break

            if selected_rarity:
                weapons_in_rarity = self.weapons_data[selected_rarity]["Weapons"]

                if weapons_in_rarity:
                    selected_weapon = random.choice(weapons_in_rarity)
                    os.system('cls')
                    WeaponGacha.anim(f"You just obtained a {selected_weapon['WeaponName']} ({selected_rarity})!")
                    self.add_item_to_inventory(selected_weapon)
        else:
            os.system('cls')
            WeaponGacha.anim("Insufficient cash!")

    def check_gacha_ticket(self):
        with open("Inventory.json", "r") as file:
            inventory = json.load(file)
        return inventory.get("GachaTickets", 0) > 0

    def use_gacha_ticket(self):
        with open("Inventory.json", "r") as file:
            inventory = json.load(file)
        inventory["GachaTickets"] -= 1
        with open("Inventory.json", "w") as file:
            json.dump(inventory, file, indent=4)


class ArmorGacha:
    def __init__(self):
        with open("Armor.json", encoding="utf8") as file:
            self.armors_data = json.load(file)

        self.drop_rates = {
            "???": 0.05,
            "Mythical": 1.95,
            "Legendary": 5.5,
            "Ultra": 10,
            "Epic": 17.5,
            "Rare": 27.5,
            "Common": 37.5
        }

    def add_item_to_inventory(self, item):
        with open("Inventory.json", "r") as file:
            inventory = json.load(file)
        if 'Armors' not in inventory:
            inventory['Armors'] = []

        if item in inventory['Armors']:
            os.system('cls')
            WeaponGacha.anim("You already have this item, so you get +350 Glowstones instead!")
            inventory['Glowstones'] = inventory.get('Glowstones', 0) + 350
        else:
            inventory['Armors'].append(item)

        with open("Inventory.json", "w") as file:
            json.dump(inventory, file, indent=4)

    def gacha(self):
        if self.check_gacha_ticket():
            self.use_gacha_ticket()
            random_number = random.uniform(0, 100)
            cumulative_probability = 0
            selected_rarity = None
            for rarity, probability in self.drop_rates.items():
                cumulative_probability += probability
                if random_number <= cumulative_probability:
                    selected_rarity = rarity
                    break

            if selected_rarity:
                armors_in_rarity = self.armors_data[selected_rarity]["Armors"]
                if armors_in_rarity:
                    selected_armor = random.choice(armors_in_rarity)
                    os.system('cls')
                    WeaponGacha.anim(f"You just obtained a {selected_armor['ArmorName']} ({selected_rarity})!")
                    self.add_item_to_inventory(selected_armor)
        else:
            os.system('cls')
            WeaponGacha.anim("Insufficient cash!")

    def check_gacha_ticket(self):
        with open("Inventory.json", "r") as file:
            inventory = json.load(file)
        return inventory.get("GachaTickets", 0) > 0

    def use_gacha_ticket(self):
        with open("Inventory.json", "r") as file:
            inventory = json.load(file)
        inventory["GachaTickets"] -= 1
        with open("Inventory.json", "w") as file:
            json.dump(inventory, file, indent=4)


class PetGacha:
    def __init__(self):
        with open("Pets.json", encoding="utf8") as file:
            self.pets_data = json.load(file)

        self.drop_rates = {
            "???": 0.05,
            "Mythical": 1.95,
            "Legendary": 5.5,
            "Ultra": 10,
            "Epic": 17.5,
            "Rare": 27.5,
            "Common": 37.5
        }

    def add_item_to_inventory(self, item):
        with open("Inventory.json", "r") as file:
            inventory = json.load(file)
        if 'Pets' not in inventory:
            inventory['Pets'] = []

        if item in inventory['Pets']:
            os.system('cls')
            WeaponGacha.anim("You already have this item, so you get +350 Glowstones instead!")
            inventory['Glowstones'] = inventory.get('Glowstones', 0) + 350
        else:
            inventory['Pets'].append(item)

        with open("Inventory.json", "w") as file:
            json.dump(inventory, file, indent=4)

    def gacha(self):
        if self.check_gacha_ticket():
            self.use_gacha_ticket()
            random_number = random.uniform(0, 100)
            cumulative_probability = 0
            selected_rarity = None
            for rarity, probability in self.drop_rates.items():
                cumulative_probability += probability
                if random_number <= cumulative_probability:
                    selected_rarity = rarity
                    break

            if selected_rarity:
                pets_in_rarity = self.pets_data[selected_rarity]["Pets"]
                if pets_in_rarity:
                    selected_pet = random.choice(pets_in_rarity)
                    os.system('cls')
                    WeaponGacha.anim(f"You just obtained a {selected_pet['PetName']} ({selected_rarity})!")
                    self.add_item_to_inventory(selected_pet)
        else:
            WeaponGacha.anim("Insufficient cash!")

    def check_gacha_ticket(self):
        with open("Inventory.json", "r") as file:
            inventory = json.load(file)
        return inventory.get("GachaTickets", 0) > 0

    def use_gacha_ticket(self):
        with open("Inventory.json", "r") as file:
            inventory = json.load(file)
        inventory["GachaTickets"] -= 1
        with open("Inventory.json", "w") as file:
            json.dump(inventory, file, indent=4)


class Shop:
    def buy_gacha_ticket(self):
        with open("Inventory.json", "r") as file:
            inventory = json.load(file)

        if inventory.get("Glowstones", 0) >= 1000:
            inventory["Glowstones"] -= 1000
            inventory["GachaTickets"] = inventory.get("GachaTickets", 0) + 1
            os.system('cls')
            WeaponGacha.anim("You have successfully bought a gacha ticket!")
        else:
            os.system('cls')
            WeaponGacha.anim("Insufficient Glowstones!")

        with open("Inventory.json", "w") as file:
            json.dump(inventory, file, indent=4)


class NPC:
    def __init__(self):
        self.weapon_gacha = WeaponGacha()
        self.armor_gacha = ArmorGacha()
        self.pet_gacha = PetGacha()
        self.shop = Shop()

    def welcome_message(self):
        WeaponGacha.anim("Welcome! What would you like to do?")
        print("1. Weapon Gacha")
        print("2. Armor Gacha")
        print("3. Pet Gacha")
        print("4. Buy Gacha Ticket")
        print("5. Exit to main map")

    def interact(self):
        while True:
            self.welcome_message()
            choice = input("Enter your choice (1/2/3/4/5): ")

            if choice == "1":
                self.weapon_gacha.gacha()
            elif choice == "2":
                self.armor_gacha.gacha()
            elif choice == "3":
                self.pet_gacha.gacha()
            elif choice == "4":
                self.shop.buy_gacha_ticket()
            elif choice == "5":
                print("Bye!")
                print("Goodbye!")
                with open("map.py", encoding="utf-8") as map_file:
                    code = map_file.read()
                exec(code)
                break
            else:
                WeaponGacha.anim("Please select 1, 2, 3, 4, or 5.")


npc = NPC()
npc.interact()
