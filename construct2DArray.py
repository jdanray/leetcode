# https://leetcode.com/problems/convert-1d-array-into-2d-array/ 

class Solution(object):
	def construct2DArray(self, original, m, n):
		if len(original) != m * n:
			return []

		res = [[0 for _ in range(n)] for _ in range(m)]
		k = 0
		for i in range(m):
			for j in range(n):
				res[i][j] = original[k]
				k += 1

		return res
