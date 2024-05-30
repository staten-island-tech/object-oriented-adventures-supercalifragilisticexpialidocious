import random, os

class Maps():
    def map(setting, setting2, enemy):
        playerCoords = [0, 1]
        mapSize = [40, 100]
        def clear(): os.system("cls")
        map = [['|' if i in [0] else '  ' for i in range(100)] for _ in range(40)]
        for row in map: 
            for i in range(2):
                row[random.randint(1, 98)] = f'{setting}' 
                if random.randint(1,5) == 1:
                    row[random.randint(1, 98)] = f"{setting2}"
                if random.randint(1,10) == 1:
                    row[random.randint(1, 98)] = f"{enemy}"

        def print_map(): 
            for row in map: 
                print(''.join(row))
                
        while True: 
            map[playerCoords[0]][playerCoords[1]] = "🟥"
            clear()
            print_map()
            whereToGo = input("Skibidimovement?: ").upper()
            if whereToGo == "W" and playerCoords[0] - 1 >= 0 and map[playerCoords[0] - 1][playerCoords[1]] not in {setting, setting2}:
                map[playerCoords[0]][playerCoords[1]] = "  " 
                playerCoords[0] -= 1
            elif whereToGo == "A" and map[playerCoords[0]][playerCoords[1] - 1] not in ["|", f"{setting}", f"{setting2}"]:
                map[playerCoords[0]][playerCoords[1]] = "  "
                playerCoords[1] -= 1
            elif whereToGo == "S" and playerCoords[0] + 1 < mapSize[0] and map[playerCoords[0] + 1][playerCoords[1]] not in {setting, setting2}:
                map[playerCoords[0]][playerCoords[1]] = "  "
                playerCoords[0] += 1
            elif whereToGo == "D" and playerCoords[1] + 1 < mapSize[1] and map[playerCoords[0]][playerCoords[1] + 1] not in ["|", f"{setting}", f"{setting2}"]:
                map[playerCoords[0]][playerCoords[1]] = "  "
                playerCoords[1] += 1
        
            if map[playerCoords[0]][playerCoords[1]] == f'{enemy}':
                print("skibidiohio")
                os.system("cls")
                break

