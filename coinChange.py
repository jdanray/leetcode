# https://leetcode.com/problems/coin-change/

class Solution:
	def coinChange(self, coins, amount):
		dp = [float('inf') for _ in range(amount + 1)]
		dp[0] = 0
		for amt in range(1, amount + 1):
			for c in coins:
				if amt - c >= 0:
					dp[amt] = min(dp[amt], dp[amt - c] + 1)
		return dp[amount] if dp[amount] < float('inf') else -1
