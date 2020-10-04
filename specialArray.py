# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/ 

class Solution(object):
	def specialArray(self, nums):
		for x in range(1, max(nums) + 1):
			count = len([n for n in nums if n >= x])
			if count == x:
				return x
            
		return -1
