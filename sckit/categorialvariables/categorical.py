#looks to sort by categorical data now 
import pandas as pd

adult_census = pd.read_csv("../datasets/adult-census.csv")
adult_census = adult_census.drop(columns="education-num")

target_name = "class"
target= adult_census[target_name]

data = adult_census.drop(columns=[target_name])

data["native-country"].value_counts().sort_index()
data.dtypes #gives the data types 

from sklearn.compose import make_column_selector as selector

categorical_columns_selector = selector(dtype_include=object)
categorical_columns = categorical_columns_selector(data)
print(categorical_columns)

data_categorical = data[categorical_columns]
print(data_categorical)

#prints out all the categorical columns 

#give each category a number- encoder 

from sklearn.preprocessing import OrdinalEncoder 

education_column = data_categorical[["education"]]

encoder = OrdinalEncoder().set_output(transform="pandas")
education_encoded = encoder.fit_transform(education_column)
print(education_encoded)
#gives a number for each column ("education" column in this case)


#hot encoder-  creates a brand new column for each category 
#use onehot encoder 
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse_output=False).set_output(transform="pandas")
education_encoded = encoder.fit_transform(education_column)
print(education_encoded)

#choosing an encoding strategy 
#onehot is good for linear models - dependent on order 
#oridinal good for tree-based models - not dependent on order 

#integrating encoder into ml

data["native-country"].values_counts()

#create machine learning pipeline

from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression

model = make_pipeline(
    OneHotEncoder(handle_unknown="ignore"), LogisticRegression(max_iter=500)
)

#now check model's generalizatino perfomrance using categorical columns 

from sklearn.model_selection import cross_validate 
cv_results = cross_validate(model, data_categorical, target)
print(cv_results) 

scores = cv_results["test_score"]
print(scores.mean())

#categorical is more predictive than numerical variables used 
