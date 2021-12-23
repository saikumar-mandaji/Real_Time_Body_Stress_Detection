from flask import Flask,render_template,request
import random

import threading
import json


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
        print(request.form.get)

        return ""

# kwargs = {'host': '0.0.0.0', 'port': 8080, 'threaded': True, 'use_reloader': False, 'debug': True}
# if __name__ == '__main__':
#     threading.Thread(target=get_w).start()
#     threading.Thread(target=app.run, daemon=True, kwargs=kwargs).start()    
app.run(host = '0.0.0.0', port= 8080,debug= True)