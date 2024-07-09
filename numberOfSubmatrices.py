# https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/ 

class Solution(object):
	def numberOfSubmatrices(self, grid):
		M = len(grid)
		N = len(grid[0])

		countX = [[0 for _ in range(N)] for _ in range(M)]
		countY = [[0 for _ in range(N)] for _ in range(M)]
		for i in range(M):
			for j in range(N):
				if j > 0:
					countX[i][j] = countX[i][j - 1]
					countY[i][j] = countY[i][j - 1]

				if grid[i][j] == 'X':
					countX[i][j] += 1
				elif grid[i][j] == 'Y':
					countY[i][j] += 1

		res = 0
		for j in range(N):
			x = 0
			y = 0
			for i in range(M):
				x += countX[i][j]
				y += countY[i][j]

				if x > 0 and x == y:
					res += 1

		return res
