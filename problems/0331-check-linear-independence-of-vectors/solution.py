import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
        
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    if len(vectors) == 0:
        return True
    def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int: # problem 329
        """
        Compute the rank of a matrix.
        
        Args:
            A: Input matrix of shape (m, n)
            tol: Tolerance for considering values as zero
        
        Returns:
            The rank of the matrix (integer)
        """
        def iszero(val):
            return abs(val) < tol
        A = A.astype(float)
        n = min(A.shape)
        p = 0
        while p<n:
            largest_value = np.argmax(abs(A[p:]), axis=0)[p] + p
            if iszero(A[largest_value,p]):
                break
            A[[largest_value,p]] = A[[p,largest_value]]
            for row in range(p+1, n):
                v = A[row,p]
                if not iszero(v):
                    A[row] -= (v/A[p,p])*A[p]
            p += 1
        return p
    return matrix_rank(np.array(vectors)) == len(vectors)