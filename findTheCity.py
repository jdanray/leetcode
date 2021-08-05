# https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution(object):
	def findTheCity(self, n, edges, distanceThreshold):
		dist = [[float('inf') for _ in range(n)] for _ in range(n)]
		
		for i in range(n):
			dist[i][i] = 0

		for (i, j, w) in edges:
			dist[i][j] = w
			dist[j][i] = w

		for k in range(n):
			for i in range(n):
				for j in range(n):
					dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

		res = -1
		mincities = float('inf')
		for i in range(n):
			cities = sum(dist[i][j] <= distanceThreshold for j in range(n))
            
			if cities <= mincities:
				mincities = cities
				res = i

		return res
