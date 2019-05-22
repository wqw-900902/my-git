from sklearn.neighbors import KNeighborsClassifier
import numpy as np

train_data=np.random.randint(12,size=24)
train_x=np.array(train_data.reshape(12,2))
print(train_x)
dict_y={1:"A",2:"B"}
train_y=np.array([dict_y[x%2+1] for x in  np.array(np.random.randint(0,train_data.size,size=12))])
print(train_y)
test_data=np.array([[3,4]])
classfiers=KNeighborsClassifier(n_neighbors=5)
classfiers.fit(train_x,train_y)
result=classfiers.predict(test_data)
print(result)
print(classfiers.predict_proba(test_data))