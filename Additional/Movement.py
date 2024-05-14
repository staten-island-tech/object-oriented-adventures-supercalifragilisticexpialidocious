import random
playerCoords  = [1,1]

mapSize = [3,125]
keybinds = ["W","A","S","D"]

def map():
    maps = []
    for i in range (1,100):
        if i in [1,99]:
            maps.append("|")
        else:
            maps.append(" ")
    maps = maps
    for i in range(1,2):
        maps[random.randint(0 , 98)] = "#"
    return maps

map_a = []

for i in range(1,25):
    map_a.append(map())

for i in map_a:
    for j in i:
        print(j, end = "")
    print("\n")

while True: 
    whereToGo = input("Where to go now?: ").capitalize() 
    while whereToGo not in keybinds: 
        whereToGo = input("Where to go now?: ").capitalize()
    
# Map2D[playerCoordinate[0]][playerCoordinate[1]] = "[ ]" 
# if whereToGo == "W": 
#     if playerCoordinate[0] - 1 >= 0: if Map2D[playerCoordinate[0] -1][playerCoordinate[1]] == "[ ]": playerCoordinate[0] -= 1 elif whereToGo == "A": if playerCoordinate[1] - 1 >= 0: if Map2D[playerCoordinate[0]][playerCoordinate[1] - 1] == "[ ]": playerCoordinate[1] -= 1 elif whereToGo == "S": if playerCoordinate[0] + 1 < mapSize[0]: if Map2D[playerCoordinate[0] + 1][playerCoordinate[1]] == "[ ]": playerCoordinate[0] += 1 elif whereToGo == "D": if playerCoordinate[1] + 1 < mapSize[1]: if Map2D[playerCoordinate[0]][playerCoordinate[1] + 1] == "[ ]": playerCoordinate[1] += 1 # Place the player at the new position Map2D[playerCoordinate[0]][playerCoordinate[1]] = "[P]" for xAxis in Map2D: print("".join(xAxis)) ```
