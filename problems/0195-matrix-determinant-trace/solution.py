def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	def determinant(mat):
		n = len(mat)
		if n == 1:
			return mat[0][0]
		elif n == 2:
			return mat[0][0]*mat[1][1]-mat[1][0]*mat[0][1]
		s = 0
		for k in range(n):
			minor = [[mat[i][j] for j in range(n) if j!=k] for i in range(1, n)]
			s += (-1)**k * mat[0][k] * determinant(minor)
		return s
	return determinant(matrix), sum(matrix[i][i] for i in range(len(matrix)))