import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def softmax(A):
    c = np.max(A)
    exp_A = np.exp(A - c)
    sum_exp_A = np.sum(exp_A)
    Y = exp_A / sum_exp_A
    return Y

def mean_squared_error(y, t):
    return 0.5 * np.sum((y-t) ** 2)

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))
