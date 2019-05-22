from sklearn.datasets import load_iris
import pandas as pd
data = load_iris()
pd_data=pd.DataFrame(data=data.data,columns=data.feature_names)
print(pd_data)
