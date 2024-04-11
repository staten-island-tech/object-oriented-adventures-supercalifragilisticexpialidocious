import json, time, random

def introduction():
    print("                                                                            :-=-::                                                                                             
                                                                             =****++=                                                                                          
                                                                              =*%#%%%#*                                                                                        
                                                                              :++#%%%%%%+                                                                                      
                                                                               :*%%%%%%%%*:                                                                                    
                                                                               :=**%%@@@@%#=                                                                                   
                                                                                =+*#%%@@@%%#+                                                                                  
                                                                                :*#*%%@@@@@%%+                                                                                 
                                            :=*%.                                **#%%%@@@@@%%*                                                                                
                           =+****+=*=*****###%#*                                 =**%%%%%%@@@%%*                                                                               
                    ::=:==+%%%%%%*%%%#%%%%@%%%*                                  +##*%%@@%@@@@@%+                                                                              
                :=++****##**#%@@@%@@@%%%%%%%%                                    =+*%%%%%@@@@@@@%*                                                                             
           .-=+**#%%%#%%%@@%%*%@@@@@@@%%%@@*                                     +**##%%@@@@@@@@@%*                                                                            
  *%****+*###%%%%@@@@%@@@@@@@%#+%%%%%%%%%*                                       =**%%%@@@@@@@@@@@%*.                                                                          
   :%%%@@@%@@@@@@@@@@@@@@@@@@@@%#+*%%%%=                                        -***###%@@@@@@@@@@%#*=                                                                         
      *%@@@@@@@@@@@@@@@@@@@@@@@@%#**+:                                          -***%%%%%@@@@@@@@@%%#*=:.                                                                      
          =%@@@@@@@@@@@@@@@@@@@@@@%%#+*++-                                 .:::-*+**#%%%%%%@@@@@%#++*%%***+++====*+=+*+====*+==.                                               
                       .-*#%%#%@@@@@%%%***=++-                      .-=+=++::.::.:+*#%%%##%%%#*#*#****##=***=*=*#***=+****=+*=**++***+==:                                      
                                *@@@@@@%%%**#*+=-.              ==+=====***+:....  +###%#%#%%%*#*#*+*#**#*+=**===+*=*++==*++*==*=**+=-===*++=:                                 
                                  #@@@%@@%%%##**=++=====-=+===*=+==****+**+*:. ..:=###**#%%#***#**###=*#***+*%*=****#+****+++*##*-=***+==+*=+++++==+*=-:::                     
                                   =@@@@@@@@@%*##***#++**+**+****#*#**##+#%*::::-#*+*###*++*              WHALECOME               +*+=+**+==*++==+==*****+=++=                 
                                     +@@@@@@@%%%%%%*#+#%#%+*#%#*%%%*%##**%%*::::#%#*##**#**#####********#*#%**%##**#***##********#*++*+*++**-+*+***+**++********=              
                                       %@@@@@@@@@@%%%%%%%#%%%%%#%%%%%%%%#%%%*-::=%##*%%%%***#%##%%%%***#%%*+*%%#******#%%##*%#%%%##*##*##***##*+*****+*+*##*#**##**:           
                                        *@@@@@@@@@@@@@%%%%%@%@%%%%%%%%%%%%%%%%%%#***%%%%#%#%%%%%%%%%**#%%%#%%%%#**%%**%%%%%%%%%%%*==*##%#*#%%##%%%%%%#%%%%%%%%%%%%%%*          
                                         .%@@@@@@@@@@@@@@%@%@%@%%@@@@@@%%%%%%%%%%%%%%%%%%%#%%%%%%%%%**%@%%%%%%%###%%##%#-               .*%%%%#%%@@@@%@@@@@@@@%%%%%%%%:        
                                           =@@@@@@@@@%=::.:=*%@@@@@@@@@@%%@@@@%@@@@%@@@@@%%%@@@@@@@%%#%@@@%%%@%%%%%%*:                    *@%%%%%@@@@@@@@@@@@@@@@@%%%%%-       
                                             *@@@@@@@           =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@%@@@%=                     #%%#%%%%%%@@@@@@@@@@@@@@@@@@%%.      
                                               %@@@@@             -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%=                -%@@%%%%@@@%%%%@@@@@@@@@@@@@@@%%      
                                                :#@@@+              %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=         =%@@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@*     
                                                   *@@=              %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%%:    
                                                     +@*             .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+.     .:%#*+==+*%@@@@@@@@@@@@@@@@@@@%@%%    
                                                       =@=            :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=                          .=*%@@@@@@@@%@%%%%    
                                                         =@%:          .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*                                      ..:=*%@%:    
                                                           -%@#..        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=     .. .               ........:::::.::::::::       
                                                              %@#...      #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+     ....:..:::......::::::::::::::::::::::...         
                                                                :#-....    =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*    ..::::::::::::::::::::::::::::::::::..              
                                                                      ..... .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%.   ..:.:::::::::::::::::::::::::::::..                   
                                                                           ..  =%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+*%#:.:::::::::::::::::::::::::::...                       
                                                                                  -#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@****%%%%%:::::::::::::::::::.....  .+%@@%%=                   
                                                                                        +#%%@@@@@@@@@@@@@@@@@@%+**#%%%%%@@%@#=...........    *%@@@@@@@@@@@@@%                  
                                                                                                             ***#%%%%%+                      #@@@@@@@@@@@@@@@@=                
                                                                                                           *+*%%%%%%%=                       *%@%%@@@@@@@@@@@@@*               
                                                                                                         -+*%@%@@@%%-                        =@@@@@@@@@@@@@@@@@@*              
                                                                                                        **#%%@@@@%%                           %@@@%@@@@@@@@@@@@@%              
                                                                                                      :*#%@@@@@@@%                             %@@@@@@@@@@@@@@@@@#             
                                                                                                     +#%%@@@@@@@%                               +@@@@@@@@@@@@@@@@@             
                                                                                                   .*%@%%@@@@@@*                                   #@@@@@@@@@@@@@@             
                                                                                                  =%@%@@@@@@@@=                                      :%@@@@@@@@@@:             
                                                                                                 #%%%@%@@@@@*                                           +#@@@@#=               
                                                                                               =%@%@%%@@@@+                                                                    
                                                                                              #@@%%%@%%%-                                                                      
                                                                                             -@@@%@%=                                                                          
                                                                                                                                                                         ")

def loadscreenpics():
    x = random.randint(1,10)
    if x == 1:
        print("              -:::    ::-:                                              ")
        print("          ::::::::::::::::::::                                          ")
        print("          :-:::::::-::::::::::                                          ")
        print("           :::-::::::-::::::-                                 ====      ")
        print("               -:-:::::-:                                   ======      ")
        print("                ::::::::                       ===================      ")
        print("                 ::::::                        ===================      ")
        print("                 :::::-                          ================       ")
        print("                  :-::                            ==============        ")
        print("                   --                               ===========         ")
        print("            ===================                         ======          ")
        print("          ==========================                    =======         ")
        print("         ==============================                 =======         ")
        print("        ==================================             ========         ")
        print("       ======================================         =========         ")
        print("       =========================================    ===========         ")
        print("      ========================================================          ")
        print("      =========================================================         ")
        print("      ===========+============================================          ")
        print("      =========*%%%*========================================--          ")
        print("      =========*%%%*=======================================--           ")
        print("      ===========+========================================-::           ")
        print("      ===================================================-::            ")
        print("       ===============================================--:::             ")
        print("       =============================================-:::::              ")
        print("        -:---==================================--::::::-                ")
        print("         ::::::::::::--------=--=-------::::::::::::::                  ")
        print("          :-::::::::::::::::::::::::::::::::::::::--                    ")
        print("            -:-:::::::::::::::::::::::::::::-::-:                       ")
        print("                 -:::::::::::------::-:-:::                             ")
    elif x == 2:
        print("")
    elif x == 3:
        print("")
    elif x == 4:
        print("")
    elif x == 5:
        print("")
    elif x == 6:
        print("")
    elif x == 7:
        print("")
    elif x == 8:
        print("")
    elif x == 9:
        print("")
    elif x == 10:
        print("")

loadscreenpics()