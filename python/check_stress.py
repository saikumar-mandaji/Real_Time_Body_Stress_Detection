#pip install pandas
import pandas as pd # To read and Process Dataset

#pip install numpy
import numpy as np #To manipulate and process dataset values

#pip install scikit-learn
from sklearn.model_selection import train_test_split #To Divide Dataset into Train and Test
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest

import pickle #To save the Trained Model
import train

#Load Pre Trained Saved Model
filename = 'model.h5'
model = pickle.load(open(filename, 'rb'))

#Get Multiplier Values from Train File
bpm_multiplier = train.bpm_multiplier
temp_multiplier = train.temp_multiplier
sr_multiplier = train.sr_multiplier

#Function to take the inputs and give output given by ML model
def check_stress(bpm,temp,sr):
    #1 means Normal
    op = model.predict([[int(bpm*bpm_multiplier),int(temp*temp_multiplier),int(sr*sr_multiplier)]])[0]
    return op

#A simple test
if __name__ == "__main__":
    print(check_stress(70,35,400))
    print(check_stress(71,36,500))
    print(check_stress(72,37,600))
    print(check_stress(73,38,700))
    print(check_stress(74,39,800))