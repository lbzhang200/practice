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

#test size - 25 percent, means 75 percent still in original set 

#using logistic regression 

from sklearn.linear_model import LogisticRegression
model = LogisticRegression() 

model.fit(data_train, target_train) #train data using training data 
accuracy = model.score(data_test, target_test) #test data using test data 
print(f"Accuracy of logistic regression: {accuracy:.3f}")

#practice 

import pandas as pd
adult_census = pd.read_csv("../datasets/adult-census.csv")

target_name = "class"
target = adult_census[target_name]
data = adult_census.drop(columns=target_name)

numerical_columns = ["age", "capital-gain", "capital-loss", "hours-per-week"]
data_numeric = data[numerical_columns]

from sklearn.model_selection import train_test_split

data_numeric_train, data_numeric_test, target_train, target_test = (
    train_test_split(data_numeric, target,random_state=42)
)

from sklearn.dummy import DummyClassifier
class_to_predict = " >50K"
high_revenue_clf = DummyClassifier(
    strategy="constant", constant= class_to_predict
)
#train and test for accuracy 
high_revenue_clf.fit(data_numeric_train, target_train)
score = high_revenue_clf.score(data_numeric_test, target_test)
print(f"Accuracy of a model predicting only high revenue: {score:.3f}")

class_to_predict = ">= 50K"
low_revenue_clf = DummyClassifier(
    strategy = "constant", constant =class_to_predict
)

low_revenue_clf.fit(data_numeric_train, target_train)
score = low_revenue_clf.score(data_numeric_test, target_test)

adult_census["class"].value_counts()

#for finding the most frequent to predict the class that appears the most in training target

most_freq_revenue_clf = DummyClassifier(strategy = "most_frequent")
most_freq_revenue_clf.fit(data_numeric_train, target_train)
score = most_freq_revenue_clf.score(data_numeric_test, target_test)
print(f"Accuracy of a model predicting the most frequent class: {score:.3f}")
