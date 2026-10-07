import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	a = np.asarray(a)
	if a.size != new_shape[0]*new_shape[1]:
		return []
	reshaped_matrix = a.reshape(*new_shape).tolist()
	return reshaped_matrix