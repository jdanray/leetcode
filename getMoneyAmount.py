# https://leetcode.com/problems/guess-number-higher-or-lower-ii/ 

class Solution(object):
	def getMoneyAmount(self, n):
		memo = {}
		def dp(start, end):
			if start >= end:
				return 0

			if (start, end) not in memo:
				memo[start, end] = min(g + max(dp(start, g - 1), dp(g + 1, end)) for g in range(start, end + 1))

			return memo[start, end]

		return dp(1, n)
