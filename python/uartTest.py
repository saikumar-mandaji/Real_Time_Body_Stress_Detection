
import serial
import time
import datetime
import tkinter as tk
import threading
import json


f = open("db.json")
dct = json.load(f)
print(dct['id'])
l3 = 0
st = 0
com = ""
def funChange(x):
    global st
    st = x

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

def getsendSMS():
    global ser
    print("sending")
    ser.write(b"otp:12345,")
    r = 0
    while 1:
        r = ser.readline()
        if len(r) > 0:
            print(r)
            break
    return r.decode('utf-8')


    
def LoginPage():
    global l3
    r=tk.Tk()
    r.geometry("600x350")
    l3 = tk.Label(r,text='WEIGHT',fg='cyan2',bg = 'blue violet')
    l3.place(x =200,y=100,height = 60,width = 200)
    b1 = tk.Button(r,text = 'CARD',fg='blue',bg = 'cyan2',command=lambda:funChange(1))
    b1.place(x =60,y=280,height = 30,width = 60)
    b2 = tk.Button(r,text = 'INDEX',fg='blue',bg = 'cyan2',command=lambda:funChange(2))
    b2.place(x =260,y=280,height = 30,width = 60)
    b3 = tk.Button(r,text = 'SMS',fg='blue',bg = 'cyan2',command=lambda:funChange(3))
    b3.place(x =460,y=280,height = 30,width = 60)
    r.mainloop()

for i in range(0,256):
    try:
        ser = serial.Serial('COM'+str(i),9600)
        #print('COM'+str(i))
        com = 'COM'+str(i)
    except :
        pass
print(com)
    
def get_w():
    global ser
    global l3
    global st
    while 1:
        if st ==1:
            l3.config(text = "TAP YOUR CARD")
            l3.config(text = getCard())
            st = 0
        if st ==2:
            l3.config(text = "place your finger")
            l3.config(text = getindex())
            st = 0
        if st ==3:
            l3.config(text = "sending sms")
            l3.config(text = getsendSMS())
            st = 0
        pass

x = 'DATE :'+str(datetime.datetime.now())
print(x)
tar1 = 0
t1 = threading.Thread(target=get_w) 
t2 = threading.Thread(target=LoginPage)
t2.start()
t1.start()

