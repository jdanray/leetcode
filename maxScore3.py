# https://leetcode.com/problems/maximum-multiplication-score/ 

class Solution(object):
	def maxScore(self, a, b):
		memo = {}
		def dp(i, j):
			if i >= len(a):
				return 0
			elif j >= len(b):
				return -float('inf')

			if (i, j) in memo:
				return memo[i, j]

			take = (a[i] * b[j]) + dp(i + 1, j + 1)
			leave = dp(i, j + 1)

			memo[i, j] = max(take, leave)
			return memo[i, j]

		return dp(0, 0)
