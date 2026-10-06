import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    result = None
    if norm_type == "l1":
        arr = arr.flatten()
        result = sum([abs(arr[i]) for i in range(arr.size)])
    elif norm_type == "l2":
        arr = arr.flatten()
        result = sum([arr[i]**2 for i in range(arr.size)])**0.5
    elif norm_type == "linf":
        arr = arr.flatten()
        result = max([abs(arr[i]) for i in range(arr.size)])
    elif norm_type == "frobenius":
        if arr.ndim != 2:
            raise ValueError("arr must be 2D")
        result = sum([sum([abs(arr[i,j])**2 for j in range(arr.shape[1])]) for i in range(arr.shape[0])])**0.5
    else:
        raise ValueError("invalid norm type")
    return float(result)