import pandas as pd
adult_census = pd.read_csv("../datasets/adult-census.csv")

#data preporcessing- scaling numerical variables 
#because if numbers are too different (age = 30 vs capital = 30k)

#basically makes the mean zero, and then look at it through standard deviations (0, 1, -1)
#data prep

target_name = "class"
target = adult_census[target_name] #target is what im trying to predict - so just this column
data = adult_census.drop(columns=target_name) #everything not in the column (the data given to help predict)

numerical_columns = ["age", "capital-gain", "capital-loss", "hours-per-week"]

data_numeric = data[numerical_columns] #data_numeric contains only numbers - KNN can only use numbers, not text 

from sklearn.model_selection import train_test_split

data_train, data_test, target_train, target_test = train_test_split(
    data_numeric, target, random_state=42
)

data_train.describe() #training data

#using data standard scaler 
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaler.fit(data_train) #trains data 

scaler.mean_ #scales mean, deviation 
scaler.scale_
data_train_scaled = scaler.transform(data_train)

print(data_train_scaled)

#can combine both 
#dont have to first scale, then use model 

import time
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

model = make_pipeline(StandardScaler(), LogisticRegression())
model.fit(data_train, target_train)
model.predict(data_test)

#automatically scales than trains - dont have to manually do each step 

#transformer vs predictor 
#predictor is like knn logistic regression- learns data and makes predictions 
#transformer is like standard scaler - learns stats from data and converts to a new form 

#transformer 
#basically takes in the mean and std of each column and produces a new value thats fair for all columns 

