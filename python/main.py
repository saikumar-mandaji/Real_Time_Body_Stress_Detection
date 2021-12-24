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
    except:
        
        return False

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
        loadF(dct)
        print(dct)
        #print(user,pw,request.form.get)

        return render_template('home.html')

# kwargs = {'host': '0.0.0.0', 'port': 8080, 'threaded': True, 'use_reloader': False, 'debug': True}
# if __name__ == '__main__':
#     threading.Thread(target=get_w).start()
#     threading.Thread(target=app.run, daemon=True, kwargs=kwargs).start()    
app.run(host = '0.0.0.0', port= 8080,debug= True)