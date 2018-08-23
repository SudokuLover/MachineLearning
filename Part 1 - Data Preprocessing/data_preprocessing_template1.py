
######################################
#Importing Library

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd


######################################
#Importing data

dataset = pd.read_csv('data.csv');
x=dataset.iloc[ : , :-1].values
y=dataset.iloc[:,3].values



######################################
#Handling Missing data

from sklearn.preprocessing import Imputer 

imputer = Imputer(missing_values='NaN',strategy= 'mean',axis=0)

#imputer = Imputer(missing_values='NaN',strategy= 'mean',axis=0)

#missing_values -> represneted by NaN
#strategy -> how to fill missing data
# axis =0 refer mean of column

imputer = imputer.fit(x[:,1:3])
#this will fit data automatically

x[:,1:3]=imputer.transform(x[:,1:3])


######################################
#Encoding Categorical data

from sklearn.preprocessing import LabelEncoder,OneHotEncoder

labelEncoder = LabelEncoder()

x[:,0] = labelEncoder.fit_transform(x[:,0])

oneHotEncoder = OneHotEncoder(categorical_features=[0])
x=oneHotEncoder.fit_transform(x).toarray()

labelEncoder_y = LabelEncoder()

y= labelEncoder_y.fit_transform(y)


######################################
#Splitting data into training set and test set

from sklearn.cross_validation import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)


#feature scaling
from sklearn.preprocessing import StandardScaler
sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)

x_test = sc_x.transform(x_test)

