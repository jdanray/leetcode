# https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution(object):
	def minOperations(self, nums):
		res = 0
		for i in range(1, len(nums)):
			if nums[i] <= nums[i - 1]:
				d = nums[i - 1] - nums[i] + 1
				nums[i] += d
				res += d

		return res
