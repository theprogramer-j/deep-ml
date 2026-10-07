import numpy as np

def polynomial_derivative(coefs: list, x: float) -> float:
    return sum([0 if n==0 else c*n*x**(n-1) for n,c in enumerate(reversed(coefs))])

def polynomial_function(coefs: list, x: float) -> float:
    return sum([c*x**n for n,c in enumerate(reversed(coefs))])

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    return (polynomial_derivative(g_coeffs, x)*polynomial_function(h_coeffs, x) - polynomial_function(g_coeffs, x)*polynomial_derivative(h_coeffs, x))/(polynomial_function(h_coeffs, x)**2)