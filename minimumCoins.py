# https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

class Solution(object):
	def minimumCoins(self, prices):
		N = len(prices)

		memo = {}
		def dp(i):
			if i > N:
				return 0

			if i in memo:
				return memo[i]

			memo[i] = prices[i - 1] + min(dp(j) for j in range(i + 1, i + i + 2))
			return memo[i]

		return dp(1)
