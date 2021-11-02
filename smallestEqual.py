# https://leetcode.com/problems/smallest-index-with-equal-value/

class Solution(object):
	def smallestEqual(self, nums):
		for i, n in enumerate(nums):
			if i % 10 == n:
				return i
            
		return -1
