import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Mycsvfile/Test.csv')
print(df.head())
df.dtypes
print(df.dtypes)

df.isnull().sum()

categorical_like = df.select_dtypes(include=['object','category','bool']).columns.to_list()
print(categorical_like)

df.drop('Item_Identifier',axis=1,inplace=True)

# Label Encoding for ordinal data

from sklearn.preprocessing import LabelEncoder

Encoder = LabelEncoder()
df['Fat_encoded'] = Encoder.fit_transform(df['Item_Fat_Content'])
df['Size_encoded'] = Encoder.fit_transform(df['Outlet_Size'])
df['Location_encode'] = Encoder.fit_transform(df['Outlet_Location_Type'])

df.drop('Item_Fat_Content',axis=1,inplace=True)
df.drop('Outlet_Size',axis=1,inplace=True)
df.drop('Outlet_Location_Type',axis=1,inplace=True)

# Frequency Encoding for nominal data

df['Item_count'] = df['Item_Type'].map(df['Item_Type'].value_counts())
df['Identifier_count'] = df['Outlet_Identifier'].map(df['Outlet_Identifier'].value_counts())
df['type_count'] = df['Outlet_Type'].map(df['Outlet_Type'].value_counts())

df.drop('Item_Type',axis=1,inplace=True)
df.drop('Outlet_Identifier',axis=1,inplace=True)
df.drop('Outlet_Type',axis=1,inplace=True)

print(df)
print(df.dtypes)

df.isnull().sum()

variables = ['Item_Weight','Item_Visibility','Size_encoded','Item_count']


for var in variables:

    plt.figure()

    sns.regplot(x=var,y='Item_MRP',data=df).set(title='Regression plot of the data')
    plt.show()
read = input("wait for me .....")

plt.figure()

correlation = df.corr()
print("correlation.....\n",correlation)

g = sns.heatmap(correlation,annot=True).set(title='The heatmap of the data')

plt.show()

read = input("wait for me .....")

print(df.columns.to_list())

cleaned_df = df[['Item_Weight','Item_Visibility','Size_encoded','Item_count','Item_MRP']].dropna()
print(cleaned_df)

X = cleaned_df[['Item_Weight','Item_Visibility','Size_encoded','Item_count']]
y = cleaned_df['Item_MRP']

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=.8,random_state=42)

from sklearn.linear_model import LinearRegression

regressor = LinearRegression()

regressor.fit(X_train,y_train)

print(regressor.intercept_)
print(regressor.coef_)

# Make prediction on test data
y_preds = regressor.predict(X_test)

result = pd.DataFrame({'Actual':y_test,'Predicted':y_preds})
print('Actual vs Predicted ....\n',result)

from sklearn.metrics import mean_absolute_error,mean_squared_error

mae =mean_absolute_error(y_test,y_preds)
mse = mean_squared_error(y_test,y_preds)
rmse = np.sqrt(mse)

print(f'Mean absolute error:{mae:.2f}')
print(f'Mean squqred error:{mse:.2f}')
print(f'Root mean squre error:{rmse:.2f}')