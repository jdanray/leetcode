# https://leetcode.com/problems/neither-minimum-nor-maximum/ 

class Solution(object):
	def findNonMinOrMax(self, nums):
		mini = min(nums)
		maxi = max(nums)
        
		for n in nums:
			if n != mini and n != maxi:
				return n
            
		return -1
