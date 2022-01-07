#pip install pandas
import pandas as pd # To read and Process Dataset

#pip install numpy
import numpy as np #To manipulate and process dataset values

#pip install scikit-learn
from sklearn.model_selection import train_test_split #To Divide Dataset into Train and Test
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest

import pickle #To save the Trained Model

#Multiplier are to scale all the values in similar range for increasing accuracy
bpm_multiplier = 1
temp_multiplier = 2
sr_multiplier = 1

def train_and_save_model(algo = 0):
    
    #Read the Dataset (csv file)
    data = pd.read_csv("data.csv") # Make sure to have atleast 1000 rows in dataset

    X = list() #Empty list to stored structured Dataset after scaling using multiplier values
    for bpm,temp,sr in zip(data['BPM'].values.tolist(), data['Temp'].values.tolist(), data['SR'].values.tolist()):
        X.append([int(bpm*bpm_multiplier),int(temp*temp_multiplier),int(sr*sr_multiplier)])

    # print(X)

    #Generating Dummy Label because we are using One Class Classifier
    Y = [1]*data.shape[0]
    
    #Diving Data into Test and Train
    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    #OPtion to use 2 different Algorithms
    if algo == 0:
        print("Using SVM Model")
        model = OneClassSVM(gamma='scale', nu=0.5) #Better Accuracy
    else:
        print("Using Isolation Tree Model")
        model = IsolationForest(n_estimators=100)
        
    model.fit(X_train) # Train the Model using Training Dataset


    #1 means Normal
    op = model.predict(X_test) # Test the Model using Test Dataset
    op = op.tolist() #Convert the Test Outputs to list
    true = op.count(1) #count right output

    accuracy = (true/len(op))*100 #Get Percentage of right output
    # print(op)
    print("Accuracy: ",accuracy, "%") # Print Model Accuracy


    #Saving the Trained Model
    filename = 'model.h5'
    pickle.dump(model, open(filename, 'wb'))
    print("Model Saved")

if __name__ == "__main__":
    train_and_save_model(0)