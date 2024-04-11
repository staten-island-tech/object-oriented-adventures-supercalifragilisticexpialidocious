import json


def Open():
    items = open("./data.json", encoding="utf8")
    inv = json.load(items)
def SaveToJson():
    with open("data.json", "w") as f:
        json_string = json.dumps(data, indent= 4)
        f.write(json_string)
