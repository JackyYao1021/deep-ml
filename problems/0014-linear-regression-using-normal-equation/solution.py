import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	X = np.array(X)
	y = np.array(y)
	theta = np.linalg.inv(X.T @ X) @ X.T @ y.T
	theta = np.round(theta, 4)
	theta[theta == 0] = 0.0
	return theta
