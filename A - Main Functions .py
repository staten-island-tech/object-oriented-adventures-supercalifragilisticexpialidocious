import time, sys, os, hashlib, json

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()

    def anim(self, text, delay=0.0375):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()

    def load_users(self):
        if os.path.exists('Users.json'):
            with open('Users.json', 'r') as file:
                self.users = json.load(file)

    def save_users(self):
        with open('Users.json', 'w') as file:
            json.dump(self.users, file, indent=4)

    def signup(self):
        username = input("E N T E R   A   U S E R N A M E :")
        
        if username in self.users:
            print("U S E R N A M E  A L R E A D Y   R E G I S T E R E D .   P I C K   A N O T H E R   O N E")
            return False
        
        password = input("E N T E R   A   P A S S W O R D : ")
        hashed_password = self._hash_password(password)
        self.users[username] = hashed_password
        self.save_users()
        print("U S E R   R E G I S T E R E D .")
        return True

    def login(self):
        username = input("U S E R N A M E :")
        
        if username not in self.users:
            print("U S E R N A M E  N O T   R E G I S T E R E D")
            return False
        
        password = input("P A S S W O R D :")
        hashed_password = self._hash_password(password)
        
        if self.users[username] == hashed_password:
            print("S U C C E S S F U L L Y   L O G G E D   I N .")
            return True
        else:
            print("I N C O R R E C T   P A S S W O R D")
            return False
        
    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()


class Game:
    cache = ""

    def anim(text, delay=0.0375):
        for char in text:
            print(char, end='', flush=True)
            time.sleep(delay)
        print()


    def changeLine(inp, index):
        sp = Game.cache.split(f"\n")
        sp[index] = inp
        Game.cache = (f"\n").join(sp)
  
    def reload():
        os.system("cls")
        print(Game.cache)

    def fullscreenprompt():
        Game.anim("\n\n")
        
        def terminalfullscreen():
            Game.anim("                                                             IS   Y O U R   T E R M I N A L   C U R R E N T L Y   O N   F U L L   S C R E E N ?    \n")
            time.sleep(1)
            a = input("                                                           ---------------------------------------------------------------------------------------    \n\n                                                                          [1] Y E S                  |                  [2] N O                         \n")
            if a == '2':
                os.system("cls")
                Game.cache = f"\n\n\n"
                Game.anim("                                            THIS GAME IS MEANT TO BE PLAYED IN FULL SCREEN — drag the top of your terminal box to the very top of your display.     \n")
                terminalfullscreen()
            elif a == '1':
                pass
            else:
                os.system("cls")
                Game.anim("\n\n\n\n\n                                                               PLEASE ONLY PICK CHOICES [1] OR [2]! - [1] for YES, and [2] for NO.     \n")
                terminalfullscreen()
                
        terminalfullscreen()

    def loadinganimation(iterations=1):
        chars = "/—\\|"
        for _ in range(iterations):
            for char in chars:
                sys.stdout.write(f"\rLoading {char}")
                sys.stdout.flush()
                time.sleep(0.25)


    def beginninggraphic():
        os.system("cls")
        Game.loadinganimation(3)
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
        print("                                                                                             -@@@%@%=                                                                          ")
        print("")
        time.sleep(1.25)
        Game.anim("T E X T   B A S E D   G A M E   P R O D U C T I O N   O F   P D . 6   W E N   Q I A N   Z H E N G   &   S A R A H   S H A O")
        time.sleep(3)
        os.system("cls")
        Game.loadinganimation(2)
        os.system("cls")                                                                                                

if __name__ == "__main__":
    game = Game()
    game.reload()
    game.anim("                                                              P L E A S E    P L A Y    O N    M A X I M U M    T E R M I N A L    W I N D O W    ")
    time.sleep(0.25)
    game.anim("\n")
    time.sleep(0.5)
    game.anim("                                                                               trigger warnings: bright flashes, jumpscares    ")
    time.sleep(1)
    game.fullscreenprompt()
    game.beginninggraphic()
    choice = input("Would you like to (1) Signup or (2) Login? ")

    if __name__ == "__main__":
        user_manager = UserManager()
        print("███╗     ██╗    ███╗       ██╗      ██████╗  ██████╗     ██╗███╗   ██╗    ██╗    ██╗    ██╗    ██╗   ██╗██████╗      █████╗  ██████╗ ██████╗")
        print("██╔╝    ███║    ╚██║       ██║     ██╔═══██╗██╔════╝     ██║████╗  ██║    ██║    ██║   ██╔╝    ██║   ██║██╔══██╗    ██╔══██╗██╔════╝██╔════╝")
        print("██║     ╚██║     ██║       ██║     ██║   ██║██║  ███╗    ██║██╔██╗ ██║    ██║ █╗ ██║  ██╔╝     ██║   ██║██████╔╝    ███████║██║     ██║     ")
        print("██║      ██║     ██║       ██║     ██║   ██║██║   ██║    ██║██║╚██╗██║    ██║███╗██║ ██╔╝      ██║   ██║██╔══██╗    ██╔══██║██║     ██║     ")
        print("███╗     ██║    ███║       ███████╗╚██████╔╝╚██████╔╝    ██║██║ ╚████║    ╚███╔███╔╝██╔╝       ╚██████╔╝██║  ██║    ██║  ██║╚██████╗╚██████╗")
        print("╚══╝     ╚═╝    ╚══╝       ╚══════╝ ╚═════╝  ╚═════╝     ╚═╝╚═╝  ╚═══╝     ╚══╝╚══╝ ╚═╝         ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝")
        print("")
        print("███╗    ██████╗     ███╗    ███████╗██╗ ██████╗ ███╗   ██╗    ██╗   ██╗██████╗     ███████╗ ██████╗ ██████╗     ███╗   ██╗███████╗██╗    ██╗     █████╗  ██████╗ ██████╗")
        print("██╔╝    ╚════██╗    ╚██║    ██╔════╝██║██╔════╝ ████╗  ██║    ██║   ██║██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗    ████╗  ██║██╔════╝██║    ██║    ██╔══██╗██╔════╝██╔════╝")
        print("██║      █████╔╝     ██║    ███████╗██║██║  ███╗██╔██╗ ██║    ██║   ██║██████╔╝    █████╗  ██║   ██║██████╔╝    ██╔██╗ ██║█████╗  ██║ █╗ ██║    ███████║██║     ██║     ")
        print("██║     ██╔═══╝      ██║    ╚════██║██║██║   ██║██║╚██╗██║    ██║   ██║██╔═══╝     ██╔══╝  ██║   ██║██╔══██╗    ██║╚██╗██║██╔══╝  ██║███╗██║    ██╔══██║██║     ██║     ")
        print("███╗    ███████╗    ███║    ███████║██║╚██████╔╝██║ ╚████║    ╚██████╔╝██║         ██║     ╚██████╔╝██║  ██║    ██║ ╚████║███████╗╚███╔███╔╝    ██║  ██║╚██████╗╚██████╗")
        choice = input("╚══╝    ╚══════╝    ╚══╝    ╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚═╝         ╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝\n")

        if choice == '1':
            user_manager.signup()
        elif choice == '2':
            user_manager.login()
        else:
            print("\n\n\n\n\n                                                               PLEASE ONLY PICK CHOICES [1] OR [2]! - [1] to SIGN UP, and [2] to LOG IN.     \n")