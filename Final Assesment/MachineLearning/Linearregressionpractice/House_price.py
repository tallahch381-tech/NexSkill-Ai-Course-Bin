import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import os

#script_dir = os.path.dirname(os.path.abspath(__file__))

#csv_path = os.path.join(script_dir'Mycsvfile/data.csv')

df = pd.read_csv('Mycsvfile/data.csv')
print(df.head())

categorical_like = df.select_dtypes(include=['object','category','bool']).columns.to_list()
print(categorical_like)

# Encode categorical data

df.drop('date',axis=1,inplace=True)
df.drop('country',axis=1,inplace=True)

df['city_count'] = df['city'].map(df['city'].value_counts())
df.drop('city',axis=1,inplace=True)

df['street_count'] = df['street'].map(df['street'].value_counts())
df.drop('street',axis=1,inplace=True)

df['state'] = df['statezip'].str[:2]
df['zip'] = df['statezip'].str[2:]
df.drop('statezip',axis=1,inplace=True)
df.drop('zip',axis=1,inplace=True)

df= pd.get_dummies(df,columns=['state'],prefix='state')
df.drop('state_WA',axis=1,inplace=True)


print(df)


X =df['bedrooms']
y =df['price']

df.plot.scatter(x='bedrooms',y='price',title='scater plot of linear regression')
plt.show()

df.dtypes
print(df.dtypes)

print('df.corr():',df.corr())

print('df.describe():',df.describe())

print("df['bedrooms']:",df['bedrooms'])
print("df['price]:",df['price'])

# the .reshape() method gives two argoment the first is the number of the columns you want and the other is the number of row

X = df['bedrooms'].values.reshape(-1,1)
y = df['price'].values.reshape(-1,1)

print("X:",X)
print("y:",y)

print(df['bedrooms'].values)
print(df['bedrooms'].values.shape)

print(X.shape)
print(X)

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=14)

print(X_train)
print(y_train)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(X_train,y_train)

print(regressor.intercept_)
print(regressor.coef_)

def calc(slope,bedrooms,intercept):
    return slope*bedrooms+intercept
score = calc(regressor.intercept_,regressor.coef_,9.5)
print(score)

# To make prediction on test data
y_preds = regressor.predict(X_test)

df_preds = pd.DataFrame({'Actual':y_test.squeeze(),'Predicted':y_preds.squeeze()})
print(df_preds)

from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

mae = mean_absolute_error(y_test,y_preds)
mse = mean_squared_error(y_test,y_preds)
rmse = np.sqrt(mse)
r2 = r2_score(y_test,y_preds)

# Also print the metric result
print(f'Mean abslute error:{mae:.2f}')
print(f'Mean squared error:{mse:.2f}')
print(f'Root mean squared error:{rmse}')
print(f'r2_secore:{r2:.2f}')