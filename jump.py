# https://leetcode.com/problems/jump-game-ii/

# top-down DP
class Solution(object):
	def jump(self, nums):
		N = len(nums)

		memo = {}
		def dp(i):
			if i >= N - 1:
				return 0

			if i in memo:
				return memo[i]

			if nums[i] == 0:
				memo[i] = float('inf')
				return memo[i]

			memo[i] = 1 + min(dp(i + j) for j in range(1, nums[i] + 1))
			return memo[i]

		return dp(0)

# bottom-up DP
class Solution(object):
	def jump(self, nums):
		N = len(nums)

		dp = [float('inf') for _ in range(N)]
		dp[0] = 0
		for i in range(1, N):
			for j in range(i):
				if j + nums[j] >= i:
					dp[i] = min(dp[i], dp[j] + 1)

		return dp[N - 1]
