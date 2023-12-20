# https://leetcode.com/problems/find-missing-and-repeated-values/ 

class Solution(object):
	def findMissingAndRepeatedValues(self, grid):
		N = len(grid)

		count = collections.Counter([grid[i][j] for i in range(N) for j in range(N)])
		res = [-1, -1]
		for n in range(1, N ** 2 + 1):
			if count[n] == 2:
				res[0] = n
			elif count[n] == 0:
				res[1] = n
		return res
