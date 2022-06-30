import pandas as pd
import serial
from time import sleep
import json
ind = False
try:
    f = open("data.csv")
    f.close()
except:
    print("file is not exist")
    ind = True
ser = 0
def check():
    for i in range(0,256):
        try:
            ser1 = serial.Serial('COM'+str(i),9600)
            print('COM'+str(i))
            com = 'COM'+str(i)
            return ser1
        except :
            pass

def get_w():
    global ser
    global dct
    global ind
    print(ind)
    n = 0
    while 1:
        try:
            data = ser.readline().decode("utf-8")
            #print(data)
            if('{"BPM":' in data):
                dct = json.loads(data)
                #print(dct)
                if(dct["BPM"] > 0):
                    print('No: ',n,'-',dct,)
                    n=n+1
                    data = pd.DataFrame([[dct["BPM"],dct["Temp"],dct["SR"]]],columns=["BPM","Temp","SR"])
                    data.to_csv("data.csv",index=False, header=ind,mode="a")
                    ind = False
                
        except Exception as e:
            ser = check()
            #print(e)
            
get_w()
