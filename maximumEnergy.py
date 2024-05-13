# https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/ 

class Solution(object):
	def maximumEnergy(self, energy, k):
		N = len(energy)

		dp = [0 for _ in range(N)] # dp[i] is amount of energy accumulated if you start at i
		res = float('-inf')
		for i in range(N - 1, -1, -1):
			if i + k < N:
				dp[i] = energy[i] + dp[i + k]
			else:
				dp[i] = energy[i]

			res = max(res, dp[i])

		return res

class Solution(object):
	def maximumEnergy(self, energy, k):
		memo = {}
		def dp(i):
			if i >= len(energy):
				return 0

			if i in memo:
				return memo[i]

			memo[i] = energy[i] + dp(i + k)
			return memo[i]

		return max(dp(i) for i in range(len(energy)))
