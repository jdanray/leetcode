# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

class Solution:
	def dominantIndex(self, nums):
		m = max(nums)
		for i in range(len(nums)):
			if nums[i] == m:
				idx = i
			elif m < nums[i] + nums[i]:
				return -1
		return idx
