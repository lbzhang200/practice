import pandas as pd

adult_census = pd.read_csv("../datasets/adult-census.csv")

target_name = "class"
target = adult_census[target_name]
data = adult_census.drop(columns=[target_name, "education-num"])

from sklearn.compose import make_column_selector as selector

numerical_columns_selector = selector(dtype_exclude=object)
categorical_columns_selector = selector(dtype_include=object)

#building the numerical/categorical columns 
numerical_columns = numerical_columns_selector(data)
categorical_columns = categorical_columns_selector(data)
