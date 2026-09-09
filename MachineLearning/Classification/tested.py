import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Mycsvfile/tested.csv')
print(df)
print(df.head())
print(df.isnull().sum())

missing_percent = (df.isnull().sum() / len(df)) * 100
print(missing_percent)

df['Age'].fillna(df['Age'].mean(),inplace=True)
df.drop('Cabin',axis=1,inplace=True)

print(df)

categorical_like = df.select_dtypes(include=['object','category','bool']).columns.tolist
print(categorical_like)

from sklearn.preprocessing import LabelEncoder

Encoder = LabelEncoder()

df['Embarked_encoded'] = Encoder.fit_transform(df['Embarked'])
df['Sex_encoded'] = df['Sex'].map({'male':0,'female':1})
df['Name_count'] = df['Name'].map(df['Name'].value_counts())

df.drop('Embarked',axis=1,inplace=True)
df.drop('Sex',axis=1,inplace=True)
df.drop('Name',axis=1,inplace=True)

print(df)

X = df[['Pclass','Age','Embarked_encoded','Sex_encoded']]
y = df['PassengerId']


from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y, train_size=.8,random_state=16)

from sklearn.linear_model import LogisticRegression

log_reg = LogisticRegression()

log_reg.fit(X_train,y_train)

y_preds = log_reg.predict(X_test)

# import the metrics classes
from sklearn import metrics

confu_metric = metrics.confusion_matrix(y_test,y_preds)
print("Model Evaluation using confusion metric:",confu_metric)


class_names = [0,1]
fig,ax = plt.subplots()
tick_marks = np.arange(len(class_names))
plt.xticks(tick_marks,class_names)
plt.yticks(tick_marks,class_names)

# create heatmap
sns.heatmap(pd.DataFrame(confu_metric),annot=True,cmap='YlGnBu',fmt='g')
ax.xaxis.set_label_position("top")
plt.tight_layout()
plt.title("confusion metric",y=1.1)
plt.xlabel('Actual')
plt.ylabel('predicted')
plt.show()

from sklearn.metrics import classification_report

print(classification_report(y_test,y_preds))