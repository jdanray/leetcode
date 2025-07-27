# https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

class Solution(object):
	def maximumMedianSum(self, nums):
		nums = sorted(nums)
		return sum(nums[-(i * 2 + 2)] for i in range(len(nums) // 3))