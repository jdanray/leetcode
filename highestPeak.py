# https://leetcode.com/problems/map-of-highest-peak/ 

class Solution(object):
	def highestPeak(self, isWater):
		M = len(isWater)
		N = len(isWater[0])

		queue = []
		height = [[-1 for _ in range(N)] for _ in range(M)]
		for i in range(M):
			for j in range(N):
				if isWater[i][j] == 1:
					height[i][j] = 0
					queue.append((i, j))

		seen = set()
		while queue:
			i, j = queue.pop(0)
			for (di, dj) in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
				k = i + di
				l = j + dj
				if k >= 0 and l >= 0 and k < M and l < N and (k, l) not in seen:
					height[k][l] = max(height[k][l], height[i][j] + 1)
					queue.append((k, l))
					seen.add((k, l))

		return height
