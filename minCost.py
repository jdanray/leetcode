# https://leetcode.com/problems/paint-house-iii/

class Solution(object):
	def minCost(self, houses, cost, m, n, target):
		memo = {}
		def dp(i, t, p):
			if i >= m:
				return 0 if t == target else float('inf')
			elif t > target:
				return float('inf')

			if (i, t, p) not in memo:
				if houses[i] == 0:
					memo[i, t, p] = min(dp(i + 1, t if c == p else t + 1, c) + cost[i][c - 1] for c in range(1, n + 1))
				else:
					memo[i, t, p] = dp(i + 1, t if houses[i] == p else t + 1, houses[i])

			return memo[i, t, p]

		res = dp(0, 0, -1)
		return res if res != float('inf') else -1
