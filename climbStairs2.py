# https://leetcode.com/problems/climbing-stairs-ii/

class Solution(object):
	def climbStairs(self, n, costs):
		J = 3

		dp = [float('inf') for _ in range(n + 1)]
		dp[0] = 0
		for i in range(1, n + 1):
			for j in range(1, J + 1):
				if i - j >= 0:
					dp[i] = min(dp[i], dp[i - j] + costs[i - j - 1] + (j ** 2))
		return dp[n]

class Solution(object):
	def climbStairs(self, n, costs):
		J = 3

		memo = {}
		def dp(i):
			if i == n:
				return 0

			if i in memo:
				return memo[i]

			res = float('inf')
			for j in range(1, J + 1):
				if i + j <= n:
					res = min(res, dp(i + j) + costs[i + j - 1] + (j ** 2))

			memo[i] = res
			return memo[i]

		return dp(0)