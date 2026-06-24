import pandas as pd

adult_consensus = pd.read_csv("../datasets/adult-census.csv")
data, target = adult_consensus.drop(columns="class"), adult_consensus["class"]

#data is withohut the class column
#target data is with the class column 

print(data.dtypes) #check all column's data types 


numerical_columns = ["age", "capital-gain", "capital-loss", "hours-per-week"]
data[numerical_columns] #gives info about those columns 

data["age"].describe() 
data_numeric = data[numerical_columns]

from sklearn.model_selection import train_test_split

data_train, data_test, target_train, target_test = train_test_split(
    data_numeric, target, random_state=42, test_size=0.25
)

print()