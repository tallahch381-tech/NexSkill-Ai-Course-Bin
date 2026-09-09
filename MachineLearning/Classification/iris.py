import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Mycsvfile/iris.csv')
print(df)
print(df.head())
print(df.describe())

print(df.isnull().sum())

categorical_like = df.select_dtypes(include=['object','category','bool']).columns.to_list()
print(categorical_like)

from sklearn.preprocessing import LabelEncoder

Encoder = LabelEncoder()
df['NewSpecies'] = Encoder.fit_transform(df['Species'])

X = df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y = df['NewSpecies']

from sklearn.model_selection import train_test_split
 
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=.8,random_state=34)

from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression()

log_reg.fit(X_train,y_train)

y_preds = log_reg.predict(X_test)

from sklearn import metrics
conf_metric = metrics.confusion_matrix(y_test,y_preds)
print("Model Evaluation using confution metrics:",conf_metric)

from sklearn.metrics import classification_report

print("the clasification report of the data:",classification_report(y_test,y_preds))