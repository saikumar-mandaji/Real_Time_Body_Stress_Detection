import json
import serial



def getCard():
    global ser
    print("sending")
    ser.write(b"getcardid")
    r = 0
    while 1:
        r = ser.readline()
        if len(r) > 0:
            r = r.decode("utf-8").split(":")[1].split(",")[0]
            print(r)
            break
    return r
    
def getindex():
    global ser
    print("sending")
    ser.write(b"getfingerindex")
    r = 0
    while 1:
        r = ser.readline()
        if len(r) > 0:
            r = int(r.decode('utf-8').split(":")[1])
            print(r)
            break
    return r

f = open("db.json")
dct = json.load(f)
f.close()
print(dct)
for i in range(0,256):
    try:
        ser = serial.Serial('COM'+str(i),9600)
        #print('COM'+str(i))
        com = 'COM'+str(i)
    except :
        pass
print(dct.keys())
while 1:
    id = getCard()
    if(id in dct.keys()):
        print(dct[id]["index"])
        if dct[id]["index"] == getindex():
            print("AUTHENTICATED")
        #print(dct[id])
    else :
        print("ID FAILLED")