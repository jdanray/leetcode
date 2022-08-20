# https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution(object):
	def largestLocal(self, grid):
		M = 3
		N = len(grid) - M + 1

		res = [[-1 for _ in range(N)] for _ in range(N)]
		for i in range(N):
			for j in range(N):
				maxi = grid[i][j]
				for k in range(M):
					for l in range(M):
						maxi = max(maxi, grid[i + k][j + l])
				res[i][j] = maxi
		return res

class Solution(object):
	def largestLocal(self, grid):
		M = 3
		N = len(grid) - M + 1

		res = [[-1 for _ in range(N)] for _ in range(N)]
		for i in range(N):
			for j in range(N):
				res[i][j] = max(grid[i + k][j + l] for k in range(M) for l in range(M))
		return res

class Solution(object):
	def largestLocal(self, grid):
		M = 3
		N = len(grid) - M + 1
		return [[max(grid[i + k][j + l] for k in range(M) for l in range(M)) for j in range(N)] for i in range(N)]
