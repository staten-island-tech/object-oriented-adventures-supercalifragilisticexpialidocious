import random, os

def clear():
    os.system("cls")

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

def showMap():
    for i in map_a:
        for j in i:
            print(j, end = "")
        print("\n")

for i in range(1,20):
    map_a.append(map())

map_a[playerCoords[0]][playerCoords[1]] = " "

while True: 
    clear()
    showMap()
    whereToGo = input("SKIBIDI: ").capitalize() 
    while whereToGo not in keybinds: 
        clear()
        showMap()
        whereToGo = input("SKIBIDI: ").capitalize()
        if whereToGo == "W":
            if playerCoords[0] - 1 >= 0:
                if map_a[playerCoords[0] -1][playerCoords[1]] == " ":
                    playerCoords[0] -= 1
        elif whereToGo == "A":
            if playerCoords[1] - 1 >= 0:
                if map_a[playerCoords[0]][playerCoords[1] - 1] == " ":
                    playerCoords[1] -= 1 
        elif whereToGo == "S":
            if playerCoords[0] + 1 < mapSize[0]:
                if map_a[playerCoords[0] + 1][playerCoords[1]] == " ":
                    playerCoords[0] += 1
        elif whereToGo == "D":
            if playerCoords[1] + 1 < mapSize[1]:
                if map_a[playerCoords[0]][playerCoords[1] + 1] == " ":
                    playerCoords[1] += 1
        
                    
        map_a[playerCoords[0]][playerCoords[1]] = "P"
        for xAxis in map_a:
                print("".join(xAxis))
        showMap()



# DEBUG PLEASPLEASPLEDSPLEAPLSPLEAPSLEPALSPELASPEALSPLEASPLEASLPEALPPLAELAELPASPLPLPLLLPLEALLSLLAESLPe