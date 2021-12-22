from flask import Flask,render_template,request
import random
import serial
import threading
import json
random_value = 0
com = ""
dict_flag = {"card":0,"index":0}
st = 0






for i in range(0,256):
    try:
        ser = serial.Serial('COM'+str(i),9600)
        #print('COM'+str(i))
        com = 'COM'+str(i)
    except :
        pass
print(com)

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


def get_w():
    global ser
    global st
    global dict_flag
    f = open("db.json")
    dct = json.load(f)
    print(dct)
    while 1:
        if st ==1:
            id = getCard()
            if(id in dct.keys()):
                print("Authenticated")
                dict_flag["card"] = 1
                st = 0
            else:
                print("tap again")
        if st ==2:
            getindex()
            st = 0
        if st ==3:
            getsendSMS()
            st = 0
        pass


app = Flask(__name__)
@app.route('/',methods=["get","post"])
def test():
    global st
    global dict_flag
    if request.method=="GET":
        st = 1
        return render_template('home.html')
    if request.method=="POST":
            if dict_flag["card"] == 0:return {"data":0}
            else:
                dict_flag["card"]=0
                return {"data":1}

   

@app.route('/check',methods=["get","post"])
def check():
    if request.method=="GET":
            return render_template('check.html')
    if request.method=="POST":
        return {"data":1}
    return ""
@app.route('/otp',methods=["get","post"])
def otp():
    global random_value
    if request.method=="GET":
        random_value = random.randint(1000,9999)
        print("Generated OTP :",random_value)
        return render_template('otpcheck.html')
    if request.method=="POST":
        try:
            otp = int(request.data.decode("utf-8"))
            print('Got OTP :',otp)
            print("Generated OTP :",random_value)
            if otp == random_value:return {"data":1}
            else :return {"data":0}
        except Exception as e:
            print(e)
            return {"data":0}
    return ""
@app.route('/change',methods=["get","post"])
def change():
    global random_value
    if request.method=="GET":
        return render_template('change.html')
    if request.method=="POST":
        try:
            pin = request.data.decode("utf-8")
            print('Got pin :',pin)
        except Exception as e:
            print(e)
    return ""

kwargs = {'host': '0.0.0.0', 'port': 8080, 'threaded': True, 'use_reloader': False, 'debug': True}
if __name__ == '__main__':
    threading.Thread(target=get_w).start()
    threading.Thread(target=app.run, daemon=True, kwargs=kwargs).start()    