# https://leetcode.com/problems/right-triangles/ 

class Solution(object):
	def numberOfRightTriangles(self, grid):
		M = len(grid)
		N = len(grid[0])

		col = [0 for _ in range(N)]
		for j in range(N):
			for i in range(M):
				col[j] += grid[i][j]

		res = 0
		for i in range(M):
			t = 0
			r = 0
			for j in range(N):
				if grid[i][j] == 1:
					res += t
					res += (col[j] - 1) * r 

					t += col[j] - 1
					r += 1

		return res
