import numpy as np
a = np.array([[1,2],[3,4]])
b = np.array([[2,1]])
print(a)
print(b.T)
print(a.dot(b.T))