import numpy as np

def make_diagonal(x):
	matrix = np.zeros((x.size, x.size))
	for i in range(x.size):
		matrix[i,i] = x[i]
	return matrix