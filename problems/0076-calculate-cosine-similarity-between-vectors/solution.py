import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	if v1.size != v2.size:
		raise ValueError("v1 and v2 must have the same size")
	if v1.size == 0:
		raise ValueError("vectors cannot be empty")
	n1 = np.sqrt(np.sum(v1**2))
	n2 = np.sqrt(np.sum(v2**2))
	if n1 == 0 or n2 == 0:
		raise ValueError("vectors cannot have zero magnitude")
	return float(np.dot(v1, v2)/(n1*n2))