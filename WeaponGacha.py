import random
import json

class WeaponGacha:
    def __init__(self):
        with open("Weapons.json", encoding="utf8") as file:
            self.weapons_data = json.load(file)

        self.drop_rates = [
            {"???": 0.05},
            {"Mythical": 1.95},
            {"Legendary": 5.5},
            {"Ultra": 10},
            {"Epic": 17.5},
            {"Rare": 27.5},
            {"Common": 37.5}
        ]

        self.weights = [0.05, 1.95, 5.5, 10, 17.5, 27.5, 37.5]

    def add_item_to_inventory(self, item):
        with open("Inventory.json", "r") as file:
            inventory = json.load(file)
        if 'Weapons' not in inventory:
            inventory['Weapons'] = []
        inventory['Weapons'].append(item)
        with open("Inventory.json", "w") as file:
            json.dump(inventory, file, indent=4)

    def gacha(self):
        print("Welcome to the Weapon Gacha!")
        choice = input("Would you like to use your gacha ticket? (yes/no): ")
        if choice.lower() == "yes":
            random_number = random.uniform(0, 100)
            cumulative_probability = 0
            selected_rarity = None
            for rarity, probability in self.drop_rates.items():
                cumulative_probability += probability
                if random_number <= cumulative_probability:
                    selected_rarity = rarity
                    break
            
            if selected_rarity:
                weapons_in_rarity = self.drop_rates[selected_rarity]
                if weapons_in_rarity:
                    selected_weapon = random.choices([self.drop_rates], weights = self.weights)
                    print(selected_weapon)
                    print(f"You just obtained a {selected_weapon['WeaponName']}!")
                    self.add_item_to_inventory(selected_weapon)
                else:
                    print("No weapons available in this rarity.")
            else:
                print("No weapon obtained.")
        elif choice.lower() == "no":
            print("Exiting gacha.")
        else:
            print("Invalid choice. Exiting gacha.")

gacha = WeaponGacha()
gacha.gacha()
