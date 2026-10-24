import numpy as np

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	vectors = np.array(vectors)

	centered_vectors = vectors - np.mean(vectors, axis=1, keepdims=True)
	cov = (centered_vectors @ centered_vectors.T) / (vectors.shape[1] - 1)
	return cov