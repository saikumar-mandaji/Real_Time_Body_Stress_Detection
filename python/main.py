from flask import Flask,render_template,request
import random

import threading
import json


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
    while 1:
        pass


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

# kwargs = {'host': '0.0.0.0', 'port': 8080, 'threaded': True, 'use_reloader': False, 'debug': True}
# if __name__ == '__main__':
#     threading.Thread(target=get_w).start()
#     threading.Thread(target=app.run, daemon=True, kwargs=kwargs).start()    
app.run(host = '0.0.0.0', port= 8080,debug= True)