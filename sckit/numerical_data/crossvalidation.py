#use of cross validation 
#for assessing the generaltzation performance of our model instead of a single train test split 

#data prep 
import pandas as pd
adult_census = pd.read_csv("../datasets/adult-census.csv")
target_name = "class"
target = adult_census[target_name]
data = adult_census.drop(columns=target_name)
numerical_columns = ["age", "capital-gain", "capital-loss", "hours-per-week"]

#creating make_pipeline tool to chain the preprocessing 
data_numeric = data[numerical_columns]
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

model = make_pipeline(StandardScaler(), LogisticRegression())

#cross_validate - allows for testing and training of different sets each time 
#splitting into multiple and average the results 

#k -fold strategy is a form of cross validation 

from sklearn.model_selection import cross_validate 

model = make_pipeline(StandardScaler(), LogisticRegression())
cv_result = cross_validate(model, data_numeric, target, cv=5)
cv_result

#cross_validate is a python dictinoary 
#contains 3 things: fit_time, score_time, test_score 

scores = cv_result["test_score"]
print(
    "The mean cross-validation accuracy is: "
    f"{scores.mean():.3f} ± {scores.std():.3f}"
)

