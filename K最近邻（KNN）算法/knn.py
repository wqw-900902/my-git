#K最近邻算法实现
import numpy as np
import operator
import matplotlib.pyplot as plt
train_x=np.array([[1,2],[2,3],[3,4],[4,5],[6,6],[7,8],[8,9],[10,11],[4,2],[5.5,6],[3.5,3],[4,1]])
# plt.scatter([x[0] for x in train_x],[x[1] for x in train_x])
# plt.show()
train_y=np.array(["A","A","B","A","A","A","B","B","A","B","B","B"])
test_data=np.array([[5,5]])

def knn(train_x,train_y,test_data,k):
    #计算测试数据与样本数据之间的距离
    dist=np.sum((test_data - train_x) **2,axis=1)**0.5
    print(dist)
    index=np.argsort(dist)
    print(index)
    classing={}
    for i in range(k):
        label=train_y[index[i]]
        #取出标签
        print(label)
        #对标签进行统计
        classing[label]=classing.get(label,0)+1
    print(classing)
    return sorted(classing.items(),key=operator.itemgetter(1),reverse=True)[0]


if __name__=="__main__":
    y=knn(train_x,train_y,test_data,5)
    print(y)