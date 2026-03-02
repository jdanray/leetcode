# https://leetcode.com/problems/minimum-cost-to-split-into-ones/

class Solution(object):
	def minCost(self, n):
		memo = {}
		def dp(n):
			if n == 1:
				return 0

			if n in memo:
				return memo[n]

			memo[n] = min(dp(a) + dp(n - a) + a * (n - a) for a in range(1, n))
			return memo[n]

		return dp(n)