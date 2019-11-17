import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset=pd.read_csv('salary_data.csv')
print(dataset)

#head, infor, shape of dataset
#get a copy of the dataset exclude last column

X=dataset.iloc[:, :-1].values

#get array pf dataset in column 1st
y=dataset.iloc[:, 1].values

#splitting data intotraining set and trest set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=1/3,random_state=0)

#Fitting Simple linear Regression into the Training set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)

#Predicting the Test set results
y_pred_5yrs=regressor.predict([[5]])
print("\n The 5 year pattern predicts:")
print(y_pred_5yrs)

print("\n The X_test pattern predicts:")
y_pred=regressor.predict(X_test)
print(y_pred)


