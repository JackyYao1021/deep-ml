import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a = np.array(matrix)
	eigenvalues = np.linalg.eigvals(a)
	return eigenvalues.tolist()