# https://leetcode.com/problems/maximum-ascending-subarray-sum/ 

class Solution(object):
	def maxAscendingSum(self, nums):
		res = nums[0]
		s = nums[0]
		for i in range(1, len(nums)):
			if nums[i] <= nums[i - 1]:
				s = 0
			s += nums[i]
			res = max(res, s)
		return res
