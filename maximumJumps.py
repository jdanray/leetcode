# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/ 

class Solution(object):
	def maximumJumps(self, nums, target):
		N = len(nums)

		dp = [-1] * N
		dp[0] = 0
		for j in range(N):
			for i in range(j):
				if dp[i] != -1 and -target <= nums[j] - nums[i] <= target:
					dp[j] = max(dp[j], 1 + dp[i])

		return dp[N - 1]
