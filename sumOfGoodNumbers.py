# https://leetcode.com/problems/sum-of-good-numbers/

class Solution(object):
	def sumOfGoodNumbers(self, nums, k):
		return sum(nums[i] if (i - k < 0 or nums[i - k] < nums[i]) and (i + k >= len(nums) or nums[i + k] < nums[i]) else 0 for i in range(len(nums)))

class Solution(object):
	def sumOfGoodNumbers(self, nums, k):
		res = 0
		for i in range(len(nums)):
			if (i - k < 0 or nums[i - k] < nums[i]) and (i + k >= len(nums) or nums[i + k] < nums[i]):
				res += nums[i]
		return res