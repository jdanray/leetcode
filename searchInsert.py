# https://leetcode.com/problems/search-insert-position/ 

class Solution(object):
	def searchInsert(self, nums, target):
		def condition(value):
			return nums[value] >= target

		left = 0
		right = len(nums)
		while left < right:
			mid = left + (right - left) // 2

			if condition(mid):
				right = mid
			else:
				left = mid + 1

		return left
