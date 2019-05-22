#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: stochastic_gradient_descent1.py

import numpy as np


np.random.seed(1)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)
X_b = np.c_[np.ones((100, 1)), X]

n_epochs = 10000
t0, t1 = 5, 500  # 超参数

m = 100


def learning_schedule(t):
    return t0 / (t + t1)


# 1, 随机初始化
theta = np.random.randn(2, 1)


for epoch in range(n_epochs):
    for i in range(m):
        # 2, 求gradient Xi.T * (Xi * theta - yi)
        #随机取出一个样本和样本所对应的y
        random_index = np.random.randint(m)
        xi = X_b[random_index:random_index+1]
        yi = y[random_index:random_index+1]
        #计算该样本的梯度
        gradients = xi.T.dot(xi.dot(theta)-yi)
        #设置学习率 迭代次数越多 学习率越小
        learning_rate = learning_schedule(epoch*m + i)
        # 3, 调整theta
        theta = theta - learning_rate * gradients

print(theta)






