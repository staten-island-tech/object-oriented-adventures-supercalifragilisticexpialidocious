import random, os, FIGHT

# def clear():
#     os.system("cls")

# playerCoords  = [1,1]
# mapSize = [3,125]
# keybinds = ["W","A","S","D"]

# def map():
#     maps = []
#     for i in range (1,100):
#         if i in [1,99]:
#             maps.append("|")
#         else:
#             maps.append(" ")
#     maps = maps
#     for i in range(1,2):
#         maps[random.randint(0 , 98)] = "#"
#     return maps

# map_a = []

# def showMap():
#     for i in map_a:
#         for j in i:
#             print(j, end = "")
#         print("\n")

# for i in range(1,20):
#     map_a.append(map())

# map_a[playerCoords[0]][playerCoords[1]] = " "

# while True: 
#     clear()
#     showMap()
#     whereToGo = None
#     while whereToGo not in keybinds: 
#         clear()
#         showMap()
#         whereToGo = input("SKIBIDI: ").capitalize()
#         map_a[playerCoords[0]][playerCoords[1]] = "P"
#         if whereToGo == "W":
#             if playerCoords[0] != 1:
#                 if map_a[playerCoords[0] -1][playerCoords[1]] == " ":
#                     playerCoords[0] -= 1
#         elif whereToGo == "A":
#             if playerCoords[1] != 1:
#                 if map_a[playerCoords[0]][playerCoords[1] - 1] == " ":
#                     playerCoords[1] -= 1 
#         elif whereToGo == "S":
#             if playerCoords[0] + 1 < mapSize[0]:
#                 if map_a[playerCoords[0] + 1][playerCoords[1]] == " ":
#                     playerCoords[0] += 1
#         elif whereToGo == "D":
#             if playerCoords[1] + 1 < mapSize[1]:
#                 if map_a[playerCoords[0]][playerCoords[1] + 1] == " ":
#                     playerCoords[1] += 1
        
                    
#         map_a[playerCoords[0]][playerCoords[1]] = "P"
#         for xAxis in map_a:
#                 print("".join(xAxis))

playerCoords = [0, 1]
mapSize = [35, 80]
keybinds = ["W", "A", "S", "D"]
def clear(): os.system("cls")
map = [['|' if i in [0] else '  ' for i in range(80)] for _ in range(35)]
for row in map: 
    for i in range(2):
        row[random.randint(1, 78)] = '🌲' 
        row[random.randint(1, 78)] = "💩"

def print_map(): 
    for row in map: 
        print(''.join(row))
        
while True: 
    map[playerCoords[0]][playerCoords[1]] = "🟥"
    clear()
    print_map()
    whereToGo = input("Skibidimovement?: ").upper()
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
    if map[playerCoords[0]][playerCoords[1]] == "💩":
            os.system("cls")
            print("                    =%%%#==========+#%%%@%+-                               ")
            print("                 +%%=                     .-#@*.                           ")
            print("              :##-                            =%=                          ")
            print("            .#%:                               -@-                         ")
            print("           -%+                                  -%-                    ")    
            print("          =%=                                    *%                        ")
            print("         =%-                                      #+                       ")
            print("        -%=                                       *%                       ")
            print("        **                                         %.                      ")
            print("       :@-                                         %.                      ")
            print("       :%                  .  .:*: ..   .:         %.                      ")
            print("       :%                 :-==+=: *+    .*#%*      %.                      ")
            print("       *#                  -*+=#+       =*==.     .%.                      ")
            print("       %=                  *- =@+       - -@*     -%.                      ")
            print("       %=                   :::.        :**=      *+                       ")
            print("       %=                                        :@.                       ")
            print("       %=                                        *%                        ")
            print("       %=                                       :%:                        ")
            print("       %*                                       #*                         ")
            print("       :%=                                     =@.           You dumbass you stepped in a pile of shit              ")
            print("        =%=                                    #*                          ")
            print("         -%*                   :::::::-+***-  :%:                          ")
            print("           *#         +%#*#%@@@*++++#@@%:    =%-                           ")
            print("           *%.                -+*++++:.      #%:                           ")
            print("         -%+                  +#*=--+*=       -%#.                         ")
            print("        +%=                      ....           -%#                        ")
            print("       ##.                                        +%+                      ")
            print("      ##                                           -%+                     ")
            print("    .%*                                              ##                    ")
            print("    *%                                                ##                   ")
            print("   =%-                                                .##                  ")
            print("   %*                                                  :@+                 ")
            print("  +#                                                    +%:                ")
            print("  #*                                                     #*                ")
            print("  #:                                                     .@=               ")
            print(" .#:                                                      *%               ")
            print(" .#:                                                      -%.              ")
            print(" .#:                                                       %+              ")
            print(" .%:                                                       #+              ")
            print(" .%:                                                       #+              ")
            print(" .%-                                                       %*              ")
            print("  **                                                       -@              ")
            break