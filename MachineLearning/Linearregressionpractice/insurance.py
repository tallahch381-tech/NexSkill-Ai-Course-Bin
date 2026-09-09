import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Mycsvfile/insurance.csv')
print(df)

print(df.isnull().sum())

categorical_like = df.select_dtypes(include=['object','category','bool']).columns.to_list()
print(categorical_like)

# Encode the categorical columns
df['sex_encoded'] = df['sex'].map({'male':0,'female':1})
df['smoker_encoded'] = df['smoker'].map({'yes':0,'no':1})
df['region_encoded'] = df['region'].map(df['region'].value_counts())

df.drop('sex',axis=1,inplace=True)
df.drop('smoker',axis=1,inplace=True)
df.drop('region',axis=1,inplace=True)

print(df)

X = df.drop(['bmi'],axis=1)
y = df['bmi']

for x in X:
    plt.figure()
    sns.regplot(x=x,y=y,data=df).set(title="The regression plot of the data")
    plt.show()
read = input("wait for me ...")

correlation = df.corr()
print(correlation)

plt.figure()
g = sns.heatmap(correlation,annot=True).set(title="The heatmap of the data")
plt.show()
read = input("wait for me ....")

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y, train_size=.8, random_state=50)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(X_train,y_train)

print(regressor.intercept_)
print(regressor.coef_)

# Make prediction on test data

y_preds = regressor.predict(X_test)

results = pd.DataFrame({'Actual':y_test,'predicted':y_preds})
print('Actual vs Predicted ....\n',results)

from sklearn.metrics import mean_absolute_error,mean_squared_error

mae = mean_absolute_error(y_test,y_preds)
mse = mean_squared_error(y_test,y_preds)
rmse = np.sqrt(mse)

print(f'Mean absolute error:{mae:.2f}')
print(f'Mean squared error:{mse:.2f}')
print(f'Root mean squre error:{rmse:.2f}')