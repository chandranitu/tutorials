import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn import random_projection

# force to cast 32 to 64

rng = pd.np.random.RandomState(0)
X = rng.rand(10, 2000)
X = pd.np.array(X, dtype='float32')
print(X.dtype)


transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
print(X_new.dtype)




