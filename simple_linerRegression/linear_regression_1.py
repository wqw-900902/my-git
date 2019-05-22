#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名: linear_regression_0.py

import numpy as np
import matplotlib.pyplot as plt

x = np.array([[1,4],[1,8],[1,5],[1,10],[1,12]])
y = np.array([[20],[50],[30],[70],[60]])
# 常规等式求解theta
theta_best = np.linalg.inv(x.T.dot(x)).dot(x.T).dot(y)
print(theta_best)

# 创建测试集里面的X1
X_new = np.array([[1,15]])
y_predict = X_new.dot(theta_best)
print(y_predict)




