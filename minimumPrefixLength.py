# https://leetcode.com/problems/minimum-prefix-removal-to-make-array-strictly-increasing/

class Solution(object):
	def minimumPrefixLength(self, nums):
		for i in range(len(nums) - 2, -1, -1):
			if nums[i] >= nums[i + 1]:
				return i + 1
		return 0