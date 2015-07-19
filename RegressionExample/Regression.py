import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
from pandas.stats.api import ols

diabetes = datasets.load_diabetes()
X1 = pd.Series(diabetes['data'][:,3])
X2 = pd.Series(diabetes['data'][:,2])
X3 = pd.Series(diabetes['data'][:,1])
X = pd.concat([X1,X2,X3], axis = 1)
print X
Y = pd.Series(diabetes['target'])

print ols(y=Y, x=X)

# plt.plot(X,Y,'bo')
# plt.show()