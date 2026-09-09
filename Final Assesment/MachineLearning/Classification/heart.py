import pandas as pd 
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

df = pd.read_csv('Mycsvfile/heart.csv')

print(df)
print(df.isnull().sum())

X = df.drop('target',axis=1)
y = df['target']

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=.8,random_state=12)

# create the clasifier object
clf = DecisionTreeClassifier()

clf.fit(X_train,y_train)

y_preds = clf.predict(X_test)

print('Acuracy:',metrics.accuracy_score(y_test,y_preds))

from sklearn.tree import  export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

dot_data = StringIO()
export_graphviz(clf,out_file=dot_data,filled=True,
                rounded=True,special_characters=True,
                feature_names=X.columns,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('heartV1.png')
Image(graph.create_png())

# create the clasifier 

clf = DecisionTreeClassifier(criterion='entropy',max_depth=3)

clf.fit(X_train,y_train)

y_preds = clf.predict(X_test)

print("Acuracy:",metrics.accuracy_score(y_test,y_preds))

from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

dot_data = StringIO()
export_graphviz(clf,out_file=dot_data,filled=True,
                rounded=True,special_characters=True,
                feature_names=X.columns,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('heartV2.png')
Image(graph.create_png())