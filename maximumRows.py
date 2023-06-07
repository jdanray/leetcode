# https://leetcode.com/problems/maximum-rows-covered-by-columns/ 

class Solution(object):
	def maximumRows(self, matrix, numSelect):
		M = len(matrix)
		N = len(matrix[0])

		@functools.cache
		def dp(c, ns, cols):
			if ns == 0:
				res = 0
				for i in range(M):
					if all(matrix[i][j] == 0 or (cols >> j) & 1 == 1 for j in range(N)):
						res += 1
				return res

			if c >= N:
				return 0

			incl = dp(c + 1, ns - 1, cols | (1 << c))
			excl = dp(c + 1, ns, cols)
            
			return max(incl, excl)

		return dp(0, numSelect, 0)
