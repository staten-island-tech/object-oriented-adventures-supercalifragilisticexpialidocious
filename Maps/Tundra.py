import random, os

playerCoords = [0, 1]
mapSize = [35, 80]
keybinds = ["W", "A", "S", "D"]
def clear(): os.system("cls")
map = [['|' if i in [0] else '  ' for i in range(80)] for _ in range(35)]
for row in map: 
        if random.randint(1,2) == 1:
            row[random.randint(1, 20)] = '🌲'
            
            row[random.randint(40, 78)] = '🌲'        
        if random.randint(1,10) == 1:
            row[random.randint(1, 20)] = "🔷"
            row[random.randint(40, 78)] = "🔷"


def print_map(): 
    for row in map: 
        print(''.join(row))
        
while True: 
    map[playerCoords[0]][playerCoords[1]] = "🟥"
    clear()
    print_map()

    whereToGo = input("Skibidmovement?: ").upper()
    if whereToGo == "W" and playerCoords[0] - 1 >= 0 and map[playerCoords[0] - 1][playerCoords[1]] not in ["🌲"]:
        map[playerCoords[0]][playerCoords[1]] = "  " 
        playerCoords[0] -= 1
    elif whereToGo == "A" and map[playerCoords[0]][playerCoords[1] - 1] not in ["|", "🌲"]:
        map[playerCoords[0]][playerCoords[1]] = "  "
        playerCoords[1] -= 1
    elif whereToGo == "S" and playerCoords[0] + 1 < mapSize[0] and map[playerCoords[0] + 1][playerCoords[1]] not in ["🌲"]:
        map[playerCoords[0]][playerCoords[1]] = "  "
        playerCoords[0] += 1
    elif whereToGo == "D" and playerCoords[1] + 1 < mapSize[1] and map[playerCoords[0]][playerCoords[1] + 1] not in ["|", "🌲"]:
        map[playerCoords[0]][playerCoords[1]] = "  "
        playerCoords[1] += 1
    if map[playerCoords[0]][playerCoords[1]] == "🔷":
        pass