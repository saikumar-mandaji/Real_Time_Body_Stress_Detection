import json
data1 = {
"saikumar":"saikumar123"
}

def loadF(data):
    try:
        with open("user_db.json","w") as jsonFile:
            json.dump(data,jsonFile)
            return True
    except:
        return False
def readF():
    try:
        f = open("user_db.json")
        data = json.load(f)
        f.close()
        return data
    except:
        return {}
#print(loadF(data1))
print(type(readF()))