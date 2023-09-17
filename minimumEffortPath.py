# https://leetcode.com/problems/path-with-minimum-effort/ 

class Solution(object):
	def minimumEffortPath(self, heights):
		deltas = [[0, 1], [0, -1], [1, 0], [-1, 0]]
		M = len(heights)
		N = len(heights[0])

		dist = {}
		for i in range(M):
			for j in range(N):
				dist[i, j] = float('inf')
		dist[0, 0] = 0
		
		pq = [(dist[0, 0], 0, 0)]
		heapq.heapify(pq)
		while pq:
			d, i, j = heapq.heappop(pq)

			for (di, dj) in deltas:
				ni = i + di
				nj = j + dj
				if ni >= 0 and ni < M and nj >= 0 and nj < N:
					e = max(dist[i, j], abs(heights[i][j] - heights[ni][nj]))
					if dist[ni, nj] > e:
						dist[ni, nj] = e
						heapq.heappush(pq, (e, ni, nj))

		return dist[M - 1, N - 1]
