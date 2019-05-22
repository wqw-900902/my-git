import matplotlib.pyplot as plt
import numpy as np
#y=theta0+theta1*x
# x_train = [100,80,120,75,60,43,140,132,63,55,74,44,88]
# y_train = [120,92,143,87,60,50,167,147,80,60,90,57,99]
# x_train=[4,8,5,10,12]
# y_train=[20,50,30,70,60]
np.random.seed(1)
x_train = np.arange(0., 10., 0.2)
m = len(x_train)  # 训练数据点数目
y_train = 2 * x_train + 5 + np.random.randn(m)
#步长
alpha = 0.001
#迭代次数
cnt = 0

#初始化参数的值，拟合函数为 y=theta0+theta1*x
theta0 = 0
theta1 = 0
#误差
error0=0
error1=0
#退出迭代的两次误差差值的阈值
epsilon=0.000001

def h(x):
    return theta1*x+theta0
#开始迭代
while True:
    cnt=cnt+1
    #用于存储梯度值
    diff = [0,0]
    #计算梯度
    for i in range(m):
        diff[0]+=h(x_train[i])-y_train[i]
        diff[1]+=(h(x_train[i])-y_train[i])*x_train[i]
    theta0=theta0-alpha/m*diff[0]
    theta1=theta1-alpha/m*diff[1]
    print("theta0",theta0,"  theta1",theta1)
    error1=0
    #计算两次迭代的误差的差值，小于阈值则退出迭代，输出拟合结果
    for i in range(len(x_train)):
        error1 += (y_train[i] - (theta0 + theta1 * x_train[i])) ** 2
    error1/=m

    if abs(error1 - error0) < epsilon:
        break
    else:
        error0 = error1

plt.plot(x_train,[h(x) for x in x_train])
plt.plot(x_train,y_train,'bo')
print(theta1,theta0)
print(cnt)
plt.show()
