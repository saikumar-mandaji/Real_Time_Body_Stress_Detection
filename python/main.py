from flask import Flask,render_template,request
import serial
import threading
import json
import check_stress

ser = 0
st = 0
dct = {'Temp': 47, 'BPM': 140, 'SR': 30}
com = 0
for i in range(0,256):
    try:
        ser = serial.Serial('COM'+str(i),9600)
        #print('COM'+str(i))
        com = 'COM'+str(i)
    except :
        pass
print(com)
def check():
    for i in range(0,256):
        try:
            ser1 = serial.Serial('COM'+str(i),9600)
            print('COM'+str(i))
            com = 'COM'+str(i)
            return ser1
        except :
            pass

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
    except Exception as e:
        print(e)
        return {}

def get_w():
    global st
    global dct
    global ser
    while 1:
        try:
            if st == 1:
                data = ser.readline().decode("utf-8")
                if('{"BPM":' in data):
                    
                    dct = json.loads(data)   
        except Exception as e:
            ser = check()
            # print(e)



app = Flask(__name__)
@app.route('/',methods=["get","post"])
def home():
    if request.method=="GET":
        return render_template('home.html')
    if request.method=="POST":
            return ""

@app.route('/signup',methods=["get","post"])
def signup():
    if request.method=="GET":
        return render_template('signup.html')
    if request.method=="POST":
        user = request.form.get("uname")
        pw =  request.form.get("pwd1")
        dct = readF()
        print(dct)
        dct[user]=pw
        print(loadF(dct))
        print(dct)
        return render_template('home.html')
@app.route('/signin',methods=["get","post"])
def signin():
    if request.method=="GET":
        return render_template('signin.html')
    if request.method=="POST":
        user,pw = request.data.decode("utf-8").split(",")
        print(user,pw)
        # user = request.form.get("uname")
        # pw =  request.form.get("pwd")
        dct = readF()
        kys = dct.keys()
        if user in kys :
            if dct[user] == pw:return {"data":1}
            else:return {"data":0}
        return {"data":0}
@app.route('/main',methods=["get","post"])
def main():
    global st
    global dct
    if request.method=="GET":
        return render_template('main.html')
    if request.method=="POST":
        
        data= request.data.decode("utf-8")
        #print(data)
        if data == 'predict':
            if st == 1:
                condition = check_stress.check_stress(dct['BPM'],dct["Temp"],dct["SR"])
                print(condition,dct)
                if condition == -1:return {"data":1}
                if condition == 1:return {"data":2}
                return {"data":1}
            else: return {"data":0}
        if data == "post":
            st = 1
            try:
                #print(dct,st)
                retdct = dct
                #retdct["Temp"] = round((retdct["Temp"]*1.8)+32,2)
                return retdct
            except:
                pass
    return {'Temp': 0, 'BPM': 0, 'SR': 0}

kwargs = {'host': '0.0.0.0', 'port': 8080, 'threaded': True, 'use_reloader': False, 'debug': True}
if __name__ == '__main__':
    threading.Thread(target=get_w).start()
    threading.Thread(target=app.run, daemon=True, kwargs=kwargs).start()    
#app.run(host = '0.0.0.0', port= 8080,debug= True)