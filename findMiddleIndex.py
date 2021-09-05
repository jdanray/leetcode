# https://leetcode.com/problems/find-the-middle-index-in-array/

class Solution(object):
	def findMiddleIndex(self, nums):
		total = sum(nums)
		left = 0
		for i, n in enumerate(nums):
			total -= n
			if left == total:
				return i
			left += n
            
		return -1
