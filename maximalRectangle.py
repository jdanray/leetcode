# https://leetcode.com/problems/maximal-rectangle/ 

class Solution(object):
	def maximalRectangle(self, matrix):
		M = len(matrix)
		N = len(matrix[0])

		left = collections.Counter()
		for j in range(N):
			for i in range(M):
				if matrix[i][j] == '1':
					left[i, j] = left[i, j - 1] + 1

		res = 0
		for i in range(M):
			for j in range(N):
				k = i
				r = left[i, j]
				while k >= 0 and matrix[k][j] == '1':
					r = min(r, left[k, j])
					res = max(res, (i - k + 1) * r)
					k -= 1

		return res
