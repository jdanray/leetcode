# https://leetcode.com/problems/find-pivot-index/description/

class Solution:
	def pivotIndex(self, nums):
		left = 0
		right = sum(nums)
		for i, n in enumerate(nums):
			right -= n
			if left == right:
				return i
			left += n
		return -1
