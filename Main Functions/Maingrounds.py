import random, os

#maingrounds
class Mainground:
    def maingrounds():
        playerCoords = [0, 1]
        mapSize = [35, 80]
        keybinds = ["W", "A", "S", "D"]
        def clear(): os.system("cls")
        map = [['|' if i in [0] else '  ' for i in range(80)] for _ in range(35)]
        for row in map: 
                if map.index(row) == 3:
                    for i in range(15,26):
                        row[i] = ". "
                    for i in range(37,50):
                        row[i] = ". "
                if map.index(row) == 0:
                    row[15] = "."
                    row[49] = " ."
                if map.index(row) == 1:
                    row[15] = "."
                    row[24] =  "A R S E N A L   A N D   G E A R"
                    row[35] = " ."
                if map.index(row) == 2:
                    row[15] = "."
                    row[49] = " ."
                if random.randint(1,2) == 1:
                    row[random.randint(1, 14)] = '🌲'
                    row[random.randint(50, 78)] = '🌲'        
                if random.randint(1,10) == 1:
                    row[random.randint(1, 14)] = "🔷"
                    row[random.randint(50, 78)] = "🔷"




        def print_map(): 
            for row in map: 
                print(''.join(row))
                
        while True: 
            map[playerCoords[0]][playerCoords[1]] = "🟥"
            clear()
            print_map()

            whereToGo = input("Skibidmovement?: ").upper()
            if whereToGo == "W" and playerCoords[0] - 1 >= 0 and map[playerCoords[0] - 1][playerCoords[1]] not in ["🌲", " .", ". ", "."]:
                map[playerCoords[0]][playerCoords[1]] = "  " 
                playerCoords[0] -= 1
            elif whereToGo == "A" and map[playerCoords[0]][playerCoords[1] - 1] not in ["|", "🌲", " .", ". ", "."]:
                map[playerCoords[0]][playerCoords[1]] = "  "
                playerCoords[1] -= 1
            elif whereToGo == "S" and playerCoords[0] + 1 < mapSize[0] and map[playerCoords[0] + 1][playerCoords[1]] not in ["🌲", " .", ". ", "."]:
                map[playerCoords[0]][playerCoords[1]] = "  "
                playerCoords[0] += 1
            elif whereToGo == "D" and playerCoords[1] + 1 < mapSize[1] and map[playerCoords[0]][playerCoords[1] + 1] not in ["|", "🌲", " .", ". ", "."]:
                map[playerCoords[0]][playerCoords[1]] = "  "
                playerCoords[1] += 1
            if map[playerCoords[0]][playerCoords[1]] == "🔷":
                print("skibidiohio")
                os.system("cls")
                break
