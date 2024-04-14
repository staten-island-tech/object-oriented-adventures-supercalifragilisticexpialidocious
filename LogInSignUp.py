import hashlib, time, json, os

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

if __name__ == "__main__":
    user_manager = UserManager()
    choice = input("Would you like to (1) Signup or (2) Login? ")

    if choice == '1':
        user_manager.signup()
    elif choice == '2':
        user_manager.login()
    else:
        print("Invalid choice. Please choose 1 or 2.")