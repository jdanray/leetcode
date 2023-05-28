# https://leetcode.com/problems/stone-game/ 

class Solution(object):
	def stoneGame(self, piles):
		memo = {}
		def dp(i, j):
			if i > j:
				return 0

			if (i, j) in memo:
				return memo[i, j]

			memo[i, j] = max(piles[i] - dp(i + 1, j), piles[j] - dp(i, j - 1))
			return memo[i, j]

		return dp(0, len(piles) - 1) > 0
