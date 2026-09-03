#using numerical and categorical numbers together

import pandas as pd
adult_census = pd.read_csv("../datasets/adult-census.csv")

target_name = "class"
target = adult_census[target_name]
data = adult_census.drop(columns=target_name)

#selecting the columns 
from sklearn.compose import make_column_selector as selector:
numerical_columns_selector = selector(dtype_exclude=object)
categorical_columns_selector = selector(dtype_include=object)

#makes the numerical columns using the data 
numerical_columns = numerical_columns_selector(data)
categorical_columns  = categorical_columns_selector(data)

from sklearn.preprocessing import OneHotEncoder, StandardScaler 

categorical_preprocessor = OneHotEncoder(handle_uknown="ignore")
numerical_preprocessor = StandardScaler()


#make the preprocessors 
from sklearn.compose import make_column_transformer 

processor = make_column_transformer(
    (categorical_preprocessor, categorical_columns)
    (numerical_preprocessor, numerical_columns)
)

#transforming 

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

model = make_pipeline(preprocessor, LogisticRegression(max_ter=500))
print(model)

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline 