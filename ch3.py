from sklearn import datatsets
import numpy as np
iris = datatsets.load_iris()
X = iris.data[:, [2,3]]
y = iris.target