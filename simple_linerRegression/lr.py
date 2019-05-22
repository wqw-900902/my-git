import numpy as np
x=np.array([4,8,5,10,12])
y=np.array([20,50,30,70,60])

def fit(x,y):
    x_mean=np.mean(x)
    y_mean=np.mean(y)
    print("x_mean= %s" %x_mean,"y_mean= %s" %y_mean)
    fenmu=0
    fenzi=0
    for i in range(len(x)):
        fenmu+=(x[i]-x_mean)**2
        fenzi+=(x[i]-x_mean)*(y[i]-y_mean)
    w=fenzi/fenmu
    b=y_mean-w*x_mean
    print(fenmu,fenzi)
    return w,b

def predict(w,b,test_x):
    return w*test_x+b

if __name__=="__main__":
    w,b=fit(x,y)
    result=predict(w,b,15)
    print(result)

