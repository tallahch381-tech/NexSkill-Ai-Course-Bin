import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import  seaborn as sns
import os 

#script_dic = os.path.dirname(os.path.abspath(__file__))

#csv_path = os.path.join(script_dic,'california_housing.csv')

df = pd.read_csv('Mycsvfile/california_housing.csv')
df.head()
print(df.head())
df.dtypes
print(df.dtypes)

df.isnull().sum()

categorical_like = df.select_dtypes(include=['object','category','bool']).columns.tolist()
print(categorical_like)

X = df['HouseAge']
y = df['Population']

df.plot.scatter(x='HouseAge',y='Population',title='scatter plot of the data')
plt.show()

print('df.corr():',df.corr())
print('describe():',df.describe())

print('df[HouseAge]:',df['HouseAge'])
print('df[Population]:',df['Population'])

# The .reshape method gives two argument the firs is the number of the columns that you want and the second is number of the rows

X = df['HouseAge'].values.reshape(-1,1)
y = df['Population'].values.reshape(-1,1)

print('X:',X)
print('y:',y)

print(df['HouseAge'].values)
print(df['HouseAge'].values.shape)

print(X.shape)
print(X)

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=.8,random_state=12)

print(X_train)
print(y_train)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(X_train,y_train)

print(regressor.intercept_)
print(regressor.coef_)

def calc(slope,HouseAge,intercept):
    return(slope*HouseAge+intercept)
score = calc(regressor.intercept_,regressor.coef_,7.8)
print(score)

# Make prediction on  test data
y_preds = regressor.predict(X_test)

df_preds = pd.DataFrame({'Actual':y_test.squeeze(),'Predicted':y_preds.squeeze()})
print(df_preds)

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

mae = mean_absolute_error(y_test,y_preds)
mse = mean_squared_error(y_test,y_preds)
rmse = np.sqrt(mse)
r2 = r2_score(y_test,y_preds)

print(f'Mean absolute error:{mae:.2f}')
print(f'Mean squared error:{mse:.2f}')
print(f'Root squared error:{rmse}')
print(f'r2_score:{r2:.2f}')