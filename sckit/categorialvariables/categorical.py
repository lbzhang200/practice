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

