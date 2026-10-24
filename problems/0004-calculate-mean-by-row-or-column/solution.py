import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	m_a = np.array(matrix)
	if mode == "row":
		means = np.mean(m_a, axis=1)
	elif mode == "column":
		means = np.mean(m_a, axis=0)
	return means