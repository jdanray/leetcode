# https://leetcode.com/problems/house-robber-ii/  

class Solution(object):
	def rob(self, nums):
		memo = {}
		def dp(i, first):
			if i >= len(nums) or (i == len(nums) - 1 and first):
				return 0

			if (i, first) not in memo:
				memo[i, first] = max(dp(i + 2, first or i == 0) + nums[i], dp(i + 1, first))
			return memo[i, first]

		return dp(0, False)
