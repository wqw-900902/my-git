import numpy as np

x = np.array([4,8,5,10,12])
y = np.array([20,50,30,70,60])

def fit(x,y):
    x_mean=np.mean(x)
    y_mean=np.mean(y)
    fenzi=0
    fenmu=0
    for i in range(x.size):
        fenzi+=(x[i]-x_mean)*(y[i]-y_mean)
        fenmu+=(x[i]-x_mean)**2
    w=fenzi/fenmu
    b=y_mean-w*x_mean
    return w,b
def predict(w,b,test_x):
    return w*test_x+b

if __name__=="__main__":
    w,b=fit(x,y)
    print(w,b)
    test_x=15
    test_y=predict(w,b,test_x)
    print(test_y)