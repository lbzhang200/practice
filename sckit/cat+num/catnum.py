#using numerical and categorical variables together 

import pandas as pd
adult_census = pd.read_csv("../datasets/adult-census.csv")

adult_census = adult_census.drop(columns="education-num")

target_name = "class"
target = adult_census[target_name]
data = adult_census.drop(columns=[target_name])

#selecting columns 

from sklearn.compose import make_column_selector as selector
numerical_columns_selector = selector(dtype_exlucde=object)
categorical_columns_selector = selector(dtype_include=object)

numerical_columns = numerical_columns_selector(data)
categorical_columns = categorical_columns_selector(data) 


#make the preprocessors 
from sklearn.preprocessing import OneHotEncoder, StandardScaler 

categorical_preprocessor = OneHotEncoder(handle_unknown="ignore")
numerical_preprocessor = StandardScaler()

from sklearn.compose import make_column_transformer

preprocessor = make_column_transformer(
    (categorical_preprocessor, categorical_columns),
    (numerical_preprocessor, numerical_columns),
)

#transforming the categorical and numerical columns 

#making a pipeline now (can be combined with a classifier)

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline 

model = make_pipeline(preprocessor, LogisticRegression(max_iter=500))
print(model)

from sklearn.model_selection import train_test_split

data_train, data_test, target_train, target_test = train_test_split(
    data, target, random_state=42
)

_ = model.fit(data_train, target_train) #training data 
model.predict(data_test)[:5] #predict first 5 based on data test 

target_test[:5]
model.score(data_test, target_test) #0.85

#evaluate using cross validation 

from sklearn.model_selection import cross_validate

cv_results = cross_validate(model, data, target, cv=5)
scores = cv_results["test_score"]
print(scores.mean()) #0.85

#this was using a lienar model, which is easy to train deploy and fast to predict 
#however you could use more advnaced model --> gradient-boosting trees

from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.preprocessing import OrdinalEncoder 

#dont have to use hot encoder- ordinalencoder is fine for trees
categorical_preprocessor = OrdinalEncoder(
    handle_unknown= "use_encoded_value", unknown_value=1
)
preprocessor = make_column_transformer(
    (categorical_preprocessor, categorical_columns), 
    remainder="passthrough",
)

model = make_pipeline(preprocessor, categorical_columns)

_ = model.fit(data_train, target_train)
model.score(data_test, target_test) #0.87
# better accuracy - gradient boosted machines 
