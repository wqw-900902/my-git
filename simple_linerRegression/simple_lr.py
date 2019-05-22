import numpy as np
x = np.array([4,8,5,10,12])
y = np.array([20,50,30,70,60])
#训练模型
def fit(x,y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    numerator = 0
    denominator = 0
    for i in range(x.size):
        numerator+=(x[i]-x_mean)*(y[i]-y_mean)
        denominator+=(x[i]-x_mean)**2

    w = numerator/denominator
    b = y_mean-w*x_mean
    return w,b
#预测
def predict(w,b,test_x):
    return w*test_x+b
if __name__=="__main__":
    w,b = fit(x,y)
    result = predict(w,b,15)
    print(w,b)
    print(result)
