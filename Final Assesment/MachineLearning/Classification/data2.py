import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

df = pd.read_csv('Mycsvfile/data (2).csv')
print(df)
print(df.isnull().sum())

categorical_like = df.select_dtypes(include=['object','category','bool']).columns.to_list()
print(categorical_like)

from sklearn.preprocessing import LabelEncoder

Encoder = LabelEncoder()

df['dignosis_encode'] = Encoder.fit_transform(df['diagnosis'])
df.drop('Unnamed: 32',axis=1,inplace=True)
df.drop('diagnosis',axis=1,inplace=True)
print(df)

# split data into x and y
X = df.drop('dignosis_encode',axis=1)
y = df['dignosis_encode']


#split data into training set and test set
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=.8,random_state=25)

# Make classifier object
clf = DecisionTreeClassifier()
# Train Desisio Tree classifier
clf.fit(X_train,y_train)
# predict the repose on test data
y_preds = clf.predict(X_test)
#Evaluate the model
print("Acuracy:",metrics.accuracy_score(y_test,y_preds))

# visualize the  descision tree

from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

print(y.unique())

dot_data = StringIO()
export_graphviz(clf,out_file=dot_data,filled=True,
                rounded=True,special_characters=True,feature_names=X.columns,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('diagnosisV1.png')
Image(graph.create_png())

"in the following example apply the decision tree with the depth_3 and also use the attribute selectin like entropy" 

# create the decision tree clasifier

clf = DecisionTreeClassifier(criterion='entropy',max_depth=3)

#train the clasifier

clf.fit(X_train,y_train)

# predict the reponse for test data

clf.predict(X_test)

# model accuracy, how often classifir is corect

print('Acuracy:',metrics.accuracy_score(y_test,y_preds))

# visualize the  decision tree

from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

dot_data = StringIO()
export_graphviz(clf,out_file=dot_data,filled=True,
                rounded=True,special_characters=True,
                feature_names=X.columns,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('diagnosisV2.png')
Image(graph.create_png())