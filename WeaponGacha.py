import random
import json

class WeaponGacha:
    def init(self):
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
            print("You already have this item, so you get +350 Glowstones instead!")
            inventory['Glowstones'] = inventory.get('Glowstones', 0) + 350
        else:
            inventory['Weapons'].append(item)

        with open("Inventory.json", "w") as file:
            json.dump(inventory, file, indent=4)

    def gacha(self):
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
                print(f"You just obtained a {selected_weapon['WeaponName']} ({selected_rarity})!")
                self.add_item_to_inventory(selected_weapon)

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
            print("You already have this item, so you get +350 Glowstones instead!")
            inventory['Glowstones'] = inventory.get('Glowstones', 0) + 350
        else:
            inventory['Armors'].append(item)

        with open("Inventory.json", "w") as file:
            json.dump(inventory, file, indent=4)

    def gacha(self):
        random_number = random.uniform(0, 100)
        cumulative_probability = 0
        selected_rarity = None
        for rarity, probability in self.drop_rates.items():
            cumulative_probability += probability
            if random_number <= cumulative_probability:
                selected_rarity = rarity
                break
        
        if selected_rarity:
            weapons_in_rarity = self.weapons_data[selected_rarity]["Armor"]

            if weapons_in_rarity:
                selected_weapon = random.choice(weapons_in_rarity)
                print(f"You just obtained a {selected_weapon['ArmorName']} ({selected_rarity})!")
                self.add_item_to_inventory(selected_weapon)

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
            print("You already have this item, so you get +350 Glowstones instead!")
            inventory['Glowstones'] = inventory.get('Glowstones', 0) + 350
        else:
            inventory['Pets'].append(item)

        with open("Inventory.json", "w") as file:
            json.dump(inventory, file, indent=4)

    def gacha(self):
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
                print(f"You just obtained a {selected_pet['PetName']} ({selected_rarity})!")
                self.add_item_to_inventory(selected_pet)

class NPC:
    def __init__(self):
        self.weapon_gacha = WeaponGacha()
        self.armor_gacha = ArmorGacha()
        self.pet_gacha = PetGacha()

    def welcome_message(self):
        print("Welcome! What would you like to do?")
        print("1. Weapon Gacha")
        print("2. Armor Gacha")
        print("3. Pet Gacha")

    def interact(self):
        self.welcome_message()
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            self.weapon_gacha.gacha()
        elif choice == "2":
            self.armor_gacha.gacha()
        elif choice == "3":
            self.pet_gacha.gacha()
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

npc = NPC()
npc.interact()
