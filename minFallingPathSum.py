# https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
	def minFallingPathSum(self, A):
		memo = {}

		def helper(row, col):
			if row >= len(A):
				return 0

			if (row, col) in memo:
				return memo[(row, col)]

			m = sys.maxsize
			for j in range(-1, 2):
				if col + j >= 0 and col + j < len(A[0]):
					m = min(m, A[row][col] + helper(row + 1, col + j))

			memo[(row, col)] = m
			return memo[(row, col)]

		return min(helper(0, col) for col in range(len(A[0])))
