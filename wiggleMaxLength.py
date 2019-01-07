# https://leetcode.com/problems/wiggle-subsequence/

class Solution(object):
	def wiggleMaxLength(self, nums):
		if not nums:
			return 0

		up = 1
		down = 1
		for i in range(1, len(nums)):
			if nums[i] > nums[i - 1]:
				up = down + 1
			elif nums[i] < nums[i - 1]:
				down = up + 1

		return max(up, down)
