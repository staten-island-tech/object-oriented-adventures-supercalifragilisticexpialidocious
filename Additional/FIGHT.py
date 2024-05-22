import time, random, os, json

def anim(text, delay=0.0375):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

class JsonRelatedEntityStuff():

    def __init__(self):
        self.Encounters = self._load_Encounters()
            
    def loadEntities(self):
        file_path = 'Encounters.json'
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}
        return {}
    
def find():
    pass
# WORK IN PROGRESS

class ENCOUNTER():
    anim("Y O U   H A V E   E N C O U N T E R E D   A")
    time.sleep(1)
    JsonRelatedEntityStuff.loadEntities()
    encounter = random.randint(1,5)

    if encounter == 1:
        x = str("Arctic Fox")
        y = find(x)
        z = (anim(x).upper)
    elif encounter == 2:
        x = str("Snow Leopard")
        y = find(x)
        z = (anim(x).upper)
    elif encounter == 3:
        x = str("Polar Bear")
        y = find(x)
        z = (anim(x).upper)
    elif encounter == 4:
        x = str("Elk")
        y = find(x)
        z = (anim(x).upper)
    elif encounter == 5:
        x = str("Eagle")
        y = find(x)
        z = (anim(x).upper)

    playerHealth = 10