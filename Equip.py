import json
import os
from tabulate import tabulate

class Equip:
    def __init__(self):
        with open("Inventory.json", "r") as file:
            self.inventory = json.load(file)

    def display_weapons(self):
        weapons = self.inventory.get("Weapons", [])
        if weapons:
            print("\nAvailable Weapons:")
            headers = ["Index", "Weapon Name", "Attack Power", "Rarity", "Description"]
            weapon_data = []
            for index, weapon in enumerate(sorted(weapons, key=lambda x: x["WeaponName"]), start=1):
                weapon_data.append([index, weapon["WeaponName"], weapon["AttackPower"], weapon["Rarity"], weapon["Description"]])
            print(tabulate(weapon_data, headers=headers, tablefmt="grid"))
        else:
            print("No weapons available in inventory.")

    def display_armors(self):
        armors = self.inventory.get("Armors", [])
        if armors:
            print("\nAvailable Armors:")
            headers = ["Index", "Armor Name", "Protection", "Rarity", "Description"]
            armor_data = []
            for index, armor in enumerate(sorted(armors, key=lambda x: x["ArmorName"]), start=1):
                armor_data.append([index, armor["ArmorName"], armor["Protection"], armor["Rarity"], armor["Description"]])
            print(tabulate(armor_data, headers=headers, tablefmt="grid"))
        else:
            print("No armors available in inventory.")

    def display_pets(self):
        pets = self.inventory.get("Pets", [])
        if pets:
            print("\nAvailable Pets:")
            headers = ["Index", "Pet Name", "Multiplier", "Rarity", "Description"]
            pet_data = []
            for index, pet in enumerate(sorted(pets, key=lambda x: x["PetName"]), start=1):
                pet_data.append([index, pet["PetName"], pet["Multiplier"], pet["Rarity"], pet["Description"]])
            print(tabulate(pet_data, headers=headers, tablefmt="grid"))
        else:
            print("No pets available in inventory.")

    def equip_weapon(self):
        self.display_weapons()
        choice = int(input("Enter the index of the weapon you want to equip: "))
        weapons = self.inventory.get("Weapons", [])
        if 1 <= choice <= len(weapons):
            equipped_weapon = weapons[choice - 1]
            print(f"\nEquipped {equipped_weapon['WeaponName']}.")
            # ??????????/
        else:
            print("Invalid index. Please select a valid index.")

    def equip_armor(self):
        self.display_armors()
        choice = int(input("Enter the index of the armor you want to equip: "))
        armors = self.inventory.get("Armors", [])
        if 1 <= choice <= len(armors):
            equipped_armor = armors[choice - 1]
            print(f"\nEquipped {equipped_armor['ArmorName']}.")
            # ??????????
        else:
            print("Invalid index. Please select a valid index.")

    def equip_pet(self):
        self.display_pets()
        choice = int(input("Enter the index of the pet you want to equip: "))
        pets = self.inventory.get("Pets", [])
        if 1 <= choice <= len(pets):
            equipped_pet = pets[choice - 1]
            print(f"\nEquipped {equipped_pet['PetName']}.")
            #????????
        else:
            print("Invalid index. Please select a valid index.")

    def go_back(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        # ??????

    def menu(self):
        while True:
            print("\nEquip Menu:")
            print("1. Equip Weapons")
            print("2. Equip Armor")
            print("3. Equip Pet")
            print("4. Go back to GachaSystem.py")

            choice = input("Enter your choice (1/2/3/4): ")
            if choice == "1":
                self.equip_weapon()
            elif choice == "2":
                self.equip_armor()
            elif choice == "3":
                self.equip_pet()
            elif choice == "4":
                self.go_back()
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    equip = Equip()
    equip.menu()
