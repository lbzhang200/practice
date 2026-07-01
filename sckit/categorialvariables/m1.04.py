#excercise using original encoder and pipeline with LogisicRegression

import pandas as pd
adult_census = pd.read_csv('../datasets/adult-census.csv')

target_name = "class"
target = adult_census[target_name]
data = adult_census.drop(columns=[target_name, "education-num"])

#autmotically select columns containing strings (object dtype)

from sklearn.compose import make_column_selector as selector

#sorting into cateogrical columns for data 
categorical_columns_selector = selector(dtype_include=object)
categorical_columns = categorical_columns_selector(data)
data_categorical = data[categorical_columns]

#pipline model 

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OrdinalEncoder 
from sklearn.linear_model import LogisticRegression

model = make_pipeline(
    OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=1), 
    LogisticRegression(max_iter=500)
)

#now evaluate 

from sklearn.model_selection import cross_validate

cv_results = cross_validate(model, data_categorical, target)
scores = cv_results["test score"]
print("cross validation accuracy is is " f"{scores.mean():.3f}") #0.76

#directly mapping from string labels to integers causes linear model to make bad assumptions 
#just chooses the most frequent 

#can be shown using the dummy classifier 

from sklearn.dummy import DummyClassifier

cv_results=cross_validate(DummyClassifier(strategy="most_frequent"), data_categorical, data)

scores = cv_results["test_score"]
print(scores.mean()) #0.76 

#so, switch to onehotencoder 

from sklearn.preprocessing import OneHotEncoder

model = make_pipeline(
    OneHotEncoder(handle_unknown="ignore"), LogisticRegression(max_iter=500)
)

cv_results = cross_validate(model, data_categorical, target)
scores = cv_results["test_score"]
print(scores.mean()) #0.833