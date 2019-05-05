# https://leetcode.com/problems/sort-an-array/

class Solution(object):
	def sortArray(self, nums):
		if not nums:
			return []

		left = [n for n in nums if n < nums[0]]
		mid = [n for n in nums if n == nums[0]]
		right = [n for n in nums if n > nums[0]]
        
		return self.sortArray(left) + mid + self.sortArray(right)
