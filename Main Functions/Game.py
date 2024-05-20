import time, sys, os, hashlib, json, Prologue
from Prologue import Dialogue, Worlds

def anim(text, delay=0.0375):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class UserManager:
    """
    Manages user accounts, including registration and login.
    """

    def __init__(self):
        self.users = self._load_users()

    def _load_users(self):
        """
        Loads user data from a JSON file.
        """
        file_path = 'users.json'
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}
        return {}

    def _save_users(self):
        """
        Saves user data to a JSON file.
        """
        file_path = 'Users.json'
        with open(file_path, 'w') as file:
            json.dump(self.users, file, indent=4)

    def _hash_password(self, password):
        """
        Hashes a password using SHA-256.
        """
        return hashlib.sha256(password.encode()).hexdigest()

    def signup(self):
        """
        Registers a new user.
        """
        username = anim(input("MAKE A USERNAME:\n\n"))
        if username in self.users:
            anim("USERNAME TAKEN. PLEASE PICK ANOTHER ONE.\n\n")
            time.sleep(2)
            self.signup()

        password = input("MAKE A PASSWORD:\n\n")
        hashed_password = self._hash_password(password)
        self.users[username] = hashed_password
        self._save_users()
        print("USER SUCCESSFULLY REGISTERED")
        return True

    def login(self):
        """
        Logs in an existing user.
        """
        username = anim(input("USERNAME:\n\n"))
        for i in self.users:
        
            if username not in i["username"]:
                anim("USER DOES NOT EXIST!\n\n")
                time.sleep(2)
                self.login()
            password = anim(input("PASSWORD:\n\n"))
            hashed_password = self._hash_password(password)
            if i["password"] == hashed_password:
                anim("LOG IN SUCCESS!")
                return True
            else:
                anim("PASSWORD IS INCORRECT")
                return False


class Game:
    cache = ""

    def changeLine(self, inp, index):
        sp = Game.cache.split(f"\n")
        sp[index] = inp
        Game.cache = (f"\n").join(sp)
  
    def reload(self):
        os.system("cls")
        print(Game.cache)

    def fullscreenprompt(self):
        anim("\n\n")
        
        def terminalfullscreen():
            anim("                                                            I S   Y O U R   T E R M I N A L   C U R R E N T L Y   O N   F U L L   S C R E E N ?    \n")
            time.sleep(1)
            a = input("                                                           ---------------------------------------------------------------------------------------    \n\n                                                                          [1] Y E S                  |                  [2] N O                         \n")
            if a == '2':
                os.system("cls")
                Game.cache = f"\n\n\n"
                anim("                                            THIS GAME IS MEANT TO BE PLAYED IN FULL SCREEN — drag the top of your terminal box to the very top of your display.     \n")
                terminalfullscreen()
            elif a == '1':
                pass
            else:
                os.system("cls")
                anim("\n\n\n\n\n                                                               PLEASE ONLY PICK CHOICES [1] OR [2]! - [1] for YES, and [2] for NO.     \n")
                terminalfullscreen()
                
        terminalfullscreen()

    def loadinganimation(self, iterations=1):
        chars = "/—\\|"
        for _ in range(iterations):
            for char in chars:
                sys.stdout.write(f"\rLoading {char}")
                sys.stdout.flush()
                time.sleep(0.25)


    def beginninggraphic(self):
        os.system("cls")
        self.loadinganimation(3)
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
        time.sleep(1.25)
        anim("T E X T   B A S E D   G A M E   P R O D U C T I O N   O F   P D . 6   W E N   Q I A N   Z H E N G   &   S A R A H   S H A O")
        time.sleep(3)
        os.system("cls")
        self.loadinganimation(2)
        os.system("cls")

if __name__ == "__main__":
    game = Game()
    game.reload()
    anim("                                                              P L E A S E    P L A Y    O N    M A X I M U M    T E R M I N A L    W I N D O W    ")
    time.sleep(0.25)
    anim("\n")
    time.sleep(0.5)
    anim("                                                                               trigger warnings: bright flashes, jumpscares    ")
    time.sleep(1)
    game.fullscreenprompt()
    game.beginninggraphic()
    
    user_manager = UserManager()
    
    """ while True:
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
            user_manager.login()
        elif choice == '2':
            while not user_manager.signup():
                pass
        elif choice == '3':
            print("E X I T I N G")
            break
        else:
            print("P L E A S E   I N P U T   E I T H E R   [1]   O R   [2]!") """

Dialogue.start()
Worlds.mainground()