from sklearn.linear_model import LinearRegression
import numpy as np
x = np.array([[4],[8],[5],[10],[12]])
y = np.array([20,50,30,70,60])
model = LinearRegression()
model.fit(x,y)
result = model.predict(15)
print(result)
print(model.intercept_)
print(model.coef_)