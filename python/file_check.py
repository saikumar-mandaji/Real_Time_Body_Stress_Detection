import json
import serial
from time import sleep

from serial.serialutil import Timeout


for i in range(0,256):
    try:
        ser = serial.Serial('COM'+str(i),9600)
        #print('COM'+str(i))
        com = 'COM'+str(i)
    except :
        pass
while 1:
    data = ser.readline().decode("utf-8")
    if('{"Temp":' in data):
        #print(data)
        dct = json.loads(data)
        print(dct)
    sleep(1)
