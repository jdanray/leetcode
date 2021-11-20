# https://leetcode.com/problems/maximum-alternating-subsequence-sum/

class Solution(object):
	def maxAlternatingSum(self, nums):
		memo = {}
		def helper(i, iseven):
			if i >= len(nums):
				return 0

			if (i, iseven) in memo:
				return memo[i, iseven]

			if iseven:
				s = helper(i + 1, False) + nums[i]
			else:
				s = helper(i + 1, True) - nums[i]

			memo[i, iseven] = max(s, helper(i + 1, iseven))
			return memo[i, iseven]

		return helper(0, True)
