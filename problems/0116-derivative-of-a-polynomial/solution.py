def poly_term_derivative(c: float, x: float, n: float) -> float:
    return 0 if n == 0 else c*n*x**(n-1)