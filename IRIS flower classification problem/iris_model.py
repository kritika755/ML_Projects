import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data=load_iris()
print(data.DESCR)

x=pd.DataFrame(data.data,columns=(data.feature_names))
y=pd.DataFrame(data.target, columns=['Target'])

x_train,x_test,y_train,y_test=train_test_split(x,y,random_state=1,test_size=0.3)

def training_model():
    model=DecisionTreeClassifier()
    trained_model=model.fit(x_train,y_train)
    return trained_model


