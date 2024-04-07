import json

with open("./inventory.json", "r") as f:
    data = json.load(f)
items = open("./data.json", encoding="utf8")
inv = json.load(items)


class Inventory:
    def inv(self):
        data.append()


with open("data.json", "w") as f:
    json_string = json.dumps(data, indent= 4)
    f.write(json_string)