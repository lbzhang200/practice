import pandas as pd
from scipy.io import arff
from sklearn.neighbors import KNeighborsClassifier

data, meta = arff.loadarff('/Users/leozhang/Downloads/phpMawTba (1).arff')
df = pd.DataFrame(data)

# fix bytes issue for ALL object columns at once
df = df.apply(lambda col: col.str.decode('utf-8') if col.dtype == object else col)

# separate target
target = df['class']
data = df.drop(columns=['class'])
data = pd.get_dummies(data)

# fit and predict
model = KNeighborsClassifier()
model.fit(data, target)

#predict method - predictor (classifiers or regressors)
#transform methodd - transformer (scalers or encoders) 

target_predicted = model.predict(data)

print(target_predicted[:5])
print(target[:5])
print(target_predicted[:5] == target[:5])
 
print(target == target_predicted.mean()) #gives success rate 


accuracy = model.score(data, target) #score method to give accuracy 
model_name = model.__class__.__name__