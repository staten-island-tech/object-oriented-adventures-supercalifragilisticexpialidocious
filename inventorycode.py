import json

class Save:
    def LoadJson(self):
        with open("./inventory.json", "r") as f:
            data = json.load(f)
    def Open(self):
        items = open("./data.json", encoding="utf8")
        inv = json.load(items)
    def SaveToJson(self):
        with open("data.json", "w") as f:
            json_string = json.dumps(data, indent= 4)
            f.write(json_string)
