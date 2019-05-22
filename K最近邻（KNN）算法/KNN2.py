import numpy as np
import operator
import matplotlib.pyplot as plt
train_data=np.random.randint(12,size=24)
train_x=train_data.reshape(12,2)
dict_y={1:"A",2:"B"}
train_y=[dict_y[x%2+1] for x in  np.array(np.random.randint(0,train_data.size,size=12))]
test_data=[[3,4]]
distence_list=[]
k=5
def knn(train_x,train_y,test_data,k):
    # for i in range(len(train_x)) :
    #     distence=np.sqrt((train_x[i][0]-test_data[0][0])**2+(train_x[i][1]-test_data[0][1])**2)
    #     distence_list.append(distence)
    distence_list=np.sum((train_x-test_data)**2,axis=1)**0.5
    index=np.argsort(distence_list)
    dict={}
    for i in range(k) :
        label=train_y[index[i]]
        dict[label]=dict.get(label,0)+1
    # label_y=sorted(dict.items(),key= lambda item : item[1],reverse=True)
    return sorted(dict.items(),key=operator.itemgetter(1),reverse=True)[0][0]
# plt.plot(train_x,'ro')
# plt.show()
if __name__=="__main__" :
    y=knn(train_x,train_y,test_data,k)
    print(y)