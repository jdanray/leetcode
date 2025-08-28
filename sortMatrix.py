# https://leetcode.com/problems/sort-matrix-by-diagonals/

class Solution(object):
	def sortMatrix(self, grid):
		N = len(grid)

		pq = []
		heapq.heapify(pq)

		# top right
		for j in range(1, N):
			for i in range(N - j):
				heapq.heappush(pq, grid[i][j + i])

			for i in range(N - j):
				n = heapq.heappop(pq)
				grid[i][j + i] = n

		# bottom left
		for i in range(N):
			for j in range(N - i):
				heapq.heappush(pq, -grid[i + j][j])

			for j in range(N - i):
				n = heapq.heappop(pq)
				grid[i + j][j] = -n


		return grid

class Solution(object):
	def sortMatrix(self, grid):
		N = len(grid)

		# top right
		for j in range(1, N):
			pq = [grid[i][j + i] for i in range(N - j)]
			pq.sort()
			for i in range(N - j):
				grid[i][j + i] = pq[i]

		# bottom left
		for i in range(N):
			pq = [grid[i + j][j] for j in range(N - i)]
			pq.sort(reverse=True)
			for j in range(N - i):
				grid[i + j][j] = pq[j]

		return grid
