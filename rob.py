# https://leetcode.com/problems/house-robber/ 

class Solution(object):
	def rob(self, nums):
		memo = {}
		def dp(i):
			if i >= len(nums):
				return 0            
			elif i not in memo:
				memo[i] = max(dp(i + 1), nums[i] + dp(i + 2))
			return memo[i]

		return dp(0)

class Solution(object):
	def rob(self, nums):
		N = len(nums)

		dp = [0 for _ in range(N)]
		dp[0] = nums[0]
		for i in range(1, N):
			if i - 2 >= 0:
				dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
			else:
				dp[i] = max(dp[i - 1], nums[i])

		return dp[N - 1]

class Solution(object):
	def rob(self, nums):
		N = len(nums)
        
		dp1 = nums[0]
		dp2 = 0
		for i in range(1, N):
			dp1, dp2 = max(dp1, nums[i] + dp2), dp1

		return dp1
