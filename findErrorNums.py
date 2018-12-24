# https://leetcode.com/problems/set-mismatch/description/

class Solution(object):
	def findErrorNums(self, nums):
		r = set(range(1, len(nums) + 1)) - set(nums)
		nums = sorted(nums)
		for i in range(len(nums) - 1):
			if nums[i] == nums[i + 1]:
				return [nums[i]] + list(r)
