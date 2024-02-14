import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import joblib

seed=42

iris_df=pd.read_csv('data/iris.csv')

x=iris_df[['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']]
y=iris_df[['Species']]


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=seed,stratify=y)

clf=KNeighborsClassifier(n_neighbors=10)
clf.fit(x_train,y_train)
y_pred=clf.predict(x_test)


accuracy=accuracy_score(y_test,y_pred)
print(f'Accuracy:',{accuracy})

joblib.dump(clf,'output_models/kn_model.sav')

