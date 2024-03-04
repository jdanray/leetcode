# https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/

class Solution(object):
	def countSubmatrices(self, grid, k):
		M = len(grid)
		N = len(grid[0])

		acc = [0 for _ in range(N)]
		res = 0
		for i in range(M):
			s = 0
			for j in range(N):
				s += grid[i][j]
				acc[j] += s
				if acc[j] <= k:
					res += 1

		return res 
