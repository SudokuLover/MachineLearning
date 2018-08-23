# Polynomial Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
""" it wont work in vector as it accepts poly_reg.fit_transform(X) matrix """
y = dataset.iloc[:, 2].values

plt.scatter(X, y, color = 'red')

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""
# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()x
y_train = sc_y.fit_transform(y_train)"""


#fitting linear regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(X,y)

#fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
"""  it return a different matrix of features of power goes 0,1,2, so on"""
poly_reg=  PolynomialFeatures(degree=4)
X_poly = poly_reg.fit_transform(X)
#now fit our new varaibale for polynomial linear regression
lin_reg_2=LinearRegression()
lin_reg_2.fit(X_poly,y)

#visualizing the Linear Regression results
plt.scatter(X,y,color='red')
plt.plot(X,lin_reg.predict(X),color='blue')
plt.title('Truth or Bluff(Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('salary')
plt.show()  

#visualizing the Polynomial Linear Regression results
plt.scatter(X,y,color='red')
#plt.plot(X,lin_reg_2.predict(X_poly),color='blue')  both are similar(down statement)
plt.plot(X,lin_reg_2.predict( poly_reg.fit_transform(X)),color='blue')
plt.title('Truth or Bluff(Polynomial Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('salary')
plt.show()  

#visualizing the Polynomial Linear Regression results with different approach
X_grid=np.arange(min(X),max(X),0.1)
X_grid=X_grid.reshape(len(X_grid),1)
plt.scatter(X,y,color='red')
#plt.plot(X,lin_reg_2.predict(X_poly),color='blue')  both are similar(down statement)
plt.plot(X_grid,lin_reg_2.predict( poly_reg.fit_transform(X_grid)),color='blue')
plt.title('Truth or Bluff(Polynomial Linear Regression)')
plt.xlabel('Position Level')
plt.ylabel('salary')
plt.show()


#Predicting a new results with Linear regression model
lin_reg.predict(6.5)

#Predicting a new results with Polynomial regression model
lin_reg_2.predict(poly_reg.fit_transform(6.5))




  