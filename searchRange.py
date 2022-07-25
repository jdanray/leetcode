# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/ 

class Solution(object):
	def searchRange(self, nums, target):
		if not nums:
			return [-1, -1]

		x = bisect.bisect_left(nums, target)
		if x < 0 or x >= len(nums) or nums[x] != target:
			return [-1, -1]

		y = bisect.bisect_right(nums, target)
		return [x, y - 1]
