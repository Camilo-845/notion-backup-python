import json


def getDataById(type, id):
    with open("./src/quickGets/data.json","r") as file:
        jsonObj = json.loads(file.read())
        if(type in jsonObj):
            for item in jsonObj[type]:
                if item["id"] == id:
                    return item["name"]
        return None
    
def addData(type, id, name):
    with open("./src/quickGets/data.json","r") as file:
        jsonObj = json.loads(file.read())
        if(type in jsonObj):
            jsonObj[type].append({"id": id, "name": name})
        open("./src/quickGets/data.json","w").write(json.dumps(jsonObj))
                