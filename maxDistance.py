# https://leetcode.com/problems/as-far-from-land-as-possible/

class Solution(object):
	def maxDistance(self, grid):
		N = len(grid)
		deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)] 

		queue = collections.deque([])
		dist = {(i, j): float('inf') for i in range(N) for j in range(N)}
		for i in range(N): 
			for j in range(N): 
				if grid[i][j] == 1:
					queue.append((i, j))
					dist[i, j] = 0

		res = -1
		seen = set()
		while queue:
			i, j = queue.popleft()

			for (di, dj) in deltas: 
				k = i + di
				l = j + dj
                
				if k < 0 or k >= N or l < 0 or l >= N or grid[k][l] != 0:
					continue

				dist[k, l] = min(dist[k, l], dist[i, j] + abs(i - k) + abs(j - l))
				res = max(res, dist[k, l])
                
				if (k, l) not in seen:
					seen.add((k, l))
					queue.append((k, l))

		return res
