import numpy as np

def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	# Your code here

	
	points = np.array(points, dtype=float)
	centroids = np.array(initial_centroids, dtype=float)
	
	for _ in range(max_iterations):
		distances = np.linalg.norm(points[:, None, :] - centroids[None, :, :], axis=2)
		labels = np.argmin(distances, axis=1)

		for i in range(k):
			cluster = points[labels == i]
			if len(cluster):
				centroids[i] = np.mean(cluster, axis=0)
	
	final_centroids = centroids

	return final_centroids.flatten()