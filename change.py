# https://leetcode.com/problems/coin-change-2/

class Solution:
	def change(self, amount, coins):
		count = [[0 for _ in range(len(coins) + 1)] for _ in range(amount + 1)]
		for j in range(len(coins) + 1):
			count[0][j] = 1
		for i in range(1, amount + 1):
			for j in range(1, len(coins) + 1):
				if coins[j - 1] > i:
					count[i][j] = count[i][j - 1]
				else:
					count[i][j] = count[i][j - 1] + count[i - coins[j - 1]][j]
		return count[amount][len(coins)]
