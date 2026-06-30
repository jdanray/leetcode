# https://leetcode.com/problems/maximum-total-sum-of-k-selected-elements/

class Solution(object):
	def maxSum(self, nums, k, mul):
		nums = sorted(nums, reverse=True)
		return sum(nums[i] * max(mul - i, 1) for i in range(k))

class Solution(object):
	def maxSum(self, nums, k, mul):
		nums = sorted(nums, reverse=True)
		s = 0
		for i in range(k):
			if mul > 1:
				s += nums[i] * mul
				mul -= 1
			else:
				s += nums[i]
		return s