import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method

	m_a = np.array(a)
	m, n = new_shape[0], new_shape[1]
	if m_a.size != np.prod(new_shape):
		return []
	m_a = m_a.reshape(new_shape)
	reshape_matrix = m_a.tolist()
	return reshape_matrix