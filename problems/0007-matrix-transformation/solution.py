import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A = np.array(A)
	T = np.array(T)
	S = np.array(S)

	try:
		if np.linalg.matrix_rank(S) < S.shape[0]:
			return -1
		transformed_matrix = np.linalg.inv(T) @ A @ S
	except:
		return -1 
	return transformed_matrix