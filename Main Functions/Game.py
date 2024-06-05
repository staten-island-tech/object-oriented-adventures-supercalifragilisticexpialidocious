import time, sys, os
from Prologue import Dialogue, Worlds

delay_input = input("Enter delay in seconds before everything starts (0 for default): ")
try:
    delay = float(delay_input)
    if delay == 0:
        delay = 0.3
    elif delay < 0:
        raise ValueError
except ValueError:
    print("Please enter a valid positive number or 0 for default delay.")
    sys.exit(1)

def anim(text, delay=0.0375):
    if delay < 0:
        raise ValueError("Delay must be a non-negative number.")
    elif delay == 0:
        print(text)
    else:
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()



class Game:
    def __init__(self, delay_input):
        self.delay_input = delay_input

    def reload(self):
        os.system("cls")

    def fullscreenprompt(self):
        anim("\n\n")
        
        def terminalfullscreen():
            if self.delay_input == 0:
                print("                                                            I S   Y O U R   T E R M I N A L   C U R R E N T L Y   O N   F U L L   S C R E E N ?    \n")
            else:
                anim("                                                            I S   Y O U R   T E R M I N A L   C U R R E N T L Y   O N   F U L L   S C R E E N ?    \n")
            time.sleep(1)
            a = input("                                                           ---------------------------------------------------------------------------------------    \n\n                                                                          [1] Y E S                  |                  [2] N O                         \n")
            if a == '2':
                os.system("cls")
                if self.delay_input == 0:
                    print("\n\n\n")
                else:
                    anim("\n\n\n")
                if self.delay_input == 0:
                    print("                                            THIS GAME IS MEANT TO BE PLAYED IN FULL SCREEN — drag the top of your terminal box to the very top of your display.     \n")
                else:
                    anim("                                            THIS GAME IS MEANT TO BE PLAYED IN FULL SCREEN — drag the top of your terminal box to the very top of your display.     \n")
                terminalfullscreen()
            elif a == '1':
                pass
            else:
                os.system("cls")
                time.sleep(self.delay_input)
                if self.delay_input == 0:
                    print("\n\n\n\n\n                                                               PLEASE ONLY PICK CHOICES [1] OR [2]! - [1] for YES, and [2] for NO.     \n")
                else:
                    anim("\n\n\n\n\n                                                               PLEASE ONLY PICK CHOICES [1] OR [2]! - [1] for YES, and [2] for NO.     \n")
                terminalfullscreen()
                
        terminalfullscreen()

    def loadinganimation(self, iterations=1, delay=0.25):
        chars = "/—\\|"
        for _ in range(iterations):
            for char in chars:
                sys.stdout.write(f"\rLoading {char}")
                sys.stdout.flush()
                time.sleep(delay)

    def beginninggraphic(self, delay=0.3):
        os.system("cls")
        self.loadinganimation(3, delay)
        os.system("cls")
        print("                                                                                    **#%%@%* ")
        print("                                                                                    =**%%%%@@%%*")  
        print("                                                                                    +##*%%@@%@@@%+")
        print(" ")                               
        print("                                            :=*%.                             ▄███████▄ ███    █▄     ▄████████    ▄████████ ███    █▄   ▄█      ███           ")
        print("                           =+****+=*=*****###%#*                              ███    ███ ███    ███   ███    ███   ███    ███ ███    ███ ███  ▀█████████▄      ")
        print("                    ::=:==+%%%%%%*%%%#%%%%@%%%*                               ███    ███ ███    ███   ███    ███   ███    █▀  ███    ███ ███▌    ▀███▀▀██      ")
        print("                :=++****##**#%@@@%@@@%%%%%%%%                                 ███    ███ ███    ███  ▄███▄▄▄▄██▀   ███        ███    ███ ███▌     ███   ▀   ███")
        print("           .-=+**#%%%#%%%@@%%*%@@@@@@@%%%@@*                                ▀█████████▀  ███    ███ ▀▀███▀▀▀▀▀   ▀███████████ ███    ███ ███▌     ███          ")
        print("  *%****+*###%%%%@@@@%@@@@@@@%#+%%%%%%%%%*                                    ███        ███    ███ ▀███████████          ███ ███    ███ ███      ███       ███")
        print("   :%%%@@@%@@@@@@@@@@@@@@@@@@@@%#+*%%%%=                                      ███        ███    ███   ███    ███    ▄█    ███ ███    ███ ███      ███                          ")
        print("      *%@@@@@@@@@@@@@@@@@@@@@@@@%#**+:                                       ▄████▀      ████████▀    ███    ███  ▄████████▀  ████████▀  █▀      ▄████▀                        ")
        print("          =%@@@@@@@@@@@@@@@@@@@@@@%%#+*++-                                                                                                                                     ")
        print("                       .-*#%%#%@@@@@%%%***=++-                      .-=+=++:                                                                                                   ")
        print("                                *@@@@@@%%%**#*+=-.              ==+=====***+:....  +###%#%#%%%*#*#*+*#**#*+=**===+*=*++==*++*==*=**+=-===*++=:                                 ")
        print("                                  #@@@%@@%%%##**=++=====-=+===*=+==****+**+*:. ..:=###**#%%#%*#*#*+***+==+****+==+****+==+****=***+==+*=+++++==+*=-:::                         ")
        print("                                   =@@@@@@@@@%*##***#++**+**+****#*#**##+#%*::::-#*+*###*++*+*+=+**+==*++=+*+=+**+==+*+=+**+==*++=+*+=+**+==*++==+==*****+=++=                 ")
        print("                                     +@@@@@@@%%%%%%*#+#%#%+*#%#*%%%*%##**%%*::::#%#*##**#**##*++*+*++**-+*+***+**#*++*+*++**-+*+***++*+*++**-+*+***+**++********=              ")
        print("                                                                        %%#%%%*-::=%##*%%%%***#%##%%%%***#%%*+*%%#******#%%##*%#%%%##*##*##***##*+*****+*+*##*#**##**:         ")
        print("                                                                          %%%%%%#***%%%%#%#%%%%%%%%%**#%%%#%%%%#**%%**%%%%=-        ==#%#*#%%##%%%%%%#%%%%%%%%%%%%%%*          ")
        print(" ▄██████▄   ▄████████    ▄████████    ▄████████ ███▄▄▄▄   ██  ▄████████    @%%%%%%%%%%%%%%#%%%%%%%%%**%@%%%%%%%###%%##%#-               .*%%%%#%%@@@@%@@@@@@@@%%%%%%%%:        ")
        print(" ███    ███ ███    ███   ███    ███   ███    ███ ███▀▀▀██▄   ███    ███     @@%@@@@%@@@@@%%%@@@@@@@%%#%@@@%%%@%%%%%%*:                    *@%%%%%@@@@@@@@@@@@@@@@@%%%%%-       ")
        print(" ███    ███ ███    █▀    ███    █▀    ███    ███ ███   ███   ███    █▀      @@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@%@@@%=                      #%%#%%%%%%@@@@@@@@@@@@@@@@@@%%.     ")
        print(" ███    ███ ███         ▄███▄▄▄       ███    ███ ███   ███   ███             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%=                 -%@@%%%%@@@%%%%@@@@@@@@@@@@@@@%%     ")
        print(" ███    ███ ███        ▀▀███▀▀▀     ▀███████████ ███   ███ ▀███████████      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=              =%@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@*    ")
        print(" ███    ███ ███    █▄    ███    █▄    ███    ███ ███   ███          ███     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@%@@%%:   ")
        print(" ███    ███ ███    ███   ███    ███   ███    ███ ███   ███    ▄█    ███     @@@@@@@@@@@@@      @@@@      @@@@@@@@@@@@@@@@@@@@@@@@@@+.     .:%#*+==+*%@@@@@@@@@@@@@@@@@@@%@%%   ")
        print("  ▀██████▀  ████████▀    ██████████   ███    █▀   ▀█   █▀   ▄████████▀     @@@@@@@@@@@@@        @         @@@@@@@@@@@@@@@@@@@@=                          .=*%@@@@@@@@%@%%%%    ")
        print("                                                                          @@@@@@@@@@@@@@                  @@@@@@@@@@@@@@@@*                                      ..:=*%@%:     ")
        print("                                                                         @@@@@@@@@@@@@@@@                @@@@@@@@@@@@@@@@=     .. .               ........:::::.::::::::       ")
        print("                                                                         ##@@@@@@@@@@@@@@@              @@@@@@@@@@@@@@+     ....:..:::......::::::::::::::::::::::...          ")
        print("                                                                           =@@@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@*    ..::::::::::::::::::::::::::::::::::..              ")
        print("                                  ▄████████ ███▄▄▄▄   ████████▄              %@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@@%.   ..:.:::::::::::::::::::::::::::::..                ")
        print("                                  ███    ███ ███▀▀▀██▄ ███   ▀███              =%@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@*+*%#:.:::::::::::::::::::::::::::...                        ")
        print("                                  ███    █▀  ███   ███ ███    ███                 -#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@****%%%%%:::::::::::::::::::.....  .+%@@%%=                   ")
        print("                                 ▄███▄▄▄     ███   ███ ███    ███                       +#%%@@@@@@@@@@@@@@@@@@%+**#%%%%%@@%@#=...........    *%@@@@@@@@@@@@@%                  ")
        print("                                ▀▀███▀▀▀     ███   ███ ███    ███                                            ***#%%%%%+                      #@@@@@@@@@@@@@@@@=                ")
        print("                                  ███    █▄  ███   ███ ███    ███                                          *+*%%%%%%%=                       *%@%%@@@@@@@@@@@@@*               ")
        print("                                  ███    ███ ███   ███ ███   ▄███                                        -+*%@%@@@%%-                        =@@@@@@@@@@@@@@@@@@*              ")
        print("                                  ██████████  ▀█   █▀  ████████▀                                        **#%%@@@@%%                           %@@@%@@@@@@@@@@@@@%              ")
        print("                                                                                                      :*#%@@@@@@@%                             %@@@@@@@@@@@@@@@@@#             ")
        print("                                                                                                     +#%%@@@@@@@%                               +@@@@@@@@@@@@@@@@@             ")
        print("                                                                                                   .*%@%%@@@@@@*                                   #@@@@@@@@@@@@@@             ")
        print("                                                                                                  =%@%@@@@@@@@=                                      :%@@@@@@@@@@:             ")
        print("                                                                                                 #%%%@%@@@@@*                                           +#@@@@#=               ")
        print("                                                                                               =%@%@%%@@@@+                                                                    ")
        print("                                                                                              #@@%%%@%%%-                                                                      ")
        print("                                                                                             -@@@%@%=                                                                          \n")
        time.sleep(delay)  # Apply delay before proceeding further
        if self.delay_input == 0:
            print("\n T E X T   B A S E D   G A M E   P R O D U C T I O N   B Y   P D . 6   W E N   Q I A N   Z H E N G   A N D   S A R A H   S H A O")
        else:
            anim("\n T E X T   B A S E D   G A M E   P R O D U C T I O N   B Y   P D . 6   W E N   Q I A N   Z H E N G   A N D   S A R A H   S H A O")

        self.loadinganimation(2, delay)  # Use loadinganimation with the same iterations
        os.system("cls")

        time.sleep(delay)  # Apply delay before proceeding further

        self.loadinganimation(2, delay)  # Use loadinganimation with the same iterations
        os.system("cls")

if __name__ == "__main__":
    os.system('cls')
    game = Game(delay)
    game.reload()
    anim("                                                              P L E A S E    P L A Y    O N    M A X I M U M    T E R M I N A L    W I N D O W    ")
    time.sleep(0.25)
    anim("\n")
    time.sleep(0.5)
    anim("                                                                               trigger warnings: bright flashes, jumpscares    ")
    time.sleep(1)
    game.fullscreenprompt()


    # Apply delay
    game.beginninggraphic(delay)
    
    # Start Dialogue and Worlds
    Dialogue.start()
    Worlds.mainground()