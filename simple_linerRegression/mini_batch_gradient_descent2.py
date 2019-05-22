#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: stochastic_gradient_descent.py

import numpy as np



X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
X_b = np.c_[np.ones((100, 1)), X]
print(X_b)

n_epochs = 10000
t0, t1 = 5, 500  # 超参数
batch_size = 10
m = 100


def learning_schedule(t):
    return t0 / (t + t1)


# 1, 随机初始化
theta = np.random.randn(2, 1)


for epoch in range(n_epochs):
    #将样本打乱顺序 可以使得每次迭代的样本都不相同
    index_list = np.arange(m)
    np.random.shuffle(index_list)
    for batch in range(int(m/batch_size)):
        # 2, 求gradient Xi.T * (Xi * theta - yi)
        index_list = index_list[batch*batch_size: batch*batch_size + batch_size]
        batch_X = X_b[index_list]
        batch_y = y[index_list]
        gradients = batch_X.T.dot(batch_X.dot(theta)-batch_y)
        learning_rate = learning_schedule(epoch * m + batch)
        # 3, 调整theta
        theta = theta - learning_rate * gradients

print(theta)






