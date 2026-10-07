import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	g = np.asarray(gradient)
	magnitude = np.sqrt(np.sum(g**2))
	if magnitude == 0:
		direction = np.zeros_like(g)
		descent_direction = np.zeros_like(g)
	else:
		direction = g / magnitude
		descent_direction = -direction
	return {"magnitude": magnitude, "direction": direction, "descent_direction": descent_direction}