from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([[4],[8],[5],[10],[12]])
y = np.array([[20],[50],[30],[70],[60]])

liner_model=LinearRegression()
liner_model.fit(x,y)
resoult=liner_model.predict(15)
print(resoult)