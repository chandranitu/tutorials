# Data Preprocessing Template

#Cost Function

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# original data set
X = [1, 2, 3]
y = [1, 2.5, 3.5]

# slope of best_fit_1 is 0.5
# slope of best_fit_2 is 1.0
# slope of best_fit_3 is 1.5

hyps = [0.5, 1.0, 1.5] 

# mutiply the original X values by the theta to produce hypothesis values for each X
def multiply_matrix(mat, theta):
    mutated = []
    for i in range(len(mat)):
        mutated.append(mat[i] * theta)
    return mutated

# calculate cost by looping each sample subtract hyp(x) from y  square the result  sum them all together
def calc_cost(m, X, y):
    total = 0
    for i in range(m):
        squared_error = (y[i] - X[i]) ** 2
        total += squared_error    
    return total * (1 / (2*m))

# calculate cost for each hypothesis
for i in range(len(hyps)):
    hyp_values = multiply_matrix(X, hyps[i])
    print("Cost for ", hyps[i], " is ", calc_cost(len(X), y, hyp_values))


##---------------2nd way

import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([[1], [2.5], [3.5]])

get_theta = lambda theta: np.array([[0, theta]])

thetas = list(map(get_theta, [0.5, 1.0, 1.5]))

X = np.hstack([np.ones([3, 1]), X])

def cost(X, y, theta):
    inner = np.power(((X @ theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))

for i in range(len(thetas)):
    print(cost(X, y, thetas[i]))
