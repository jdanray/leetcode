# https://leetcode.com/problems/find-the-value-of-the-partition/ 

class Solution(object):
	def findValueOfPartition(self, nums):
		nums = sorted(nums)
		res = float('inf')
		for i in range(1, len(nums)):
			res = min(res, nums[i] - nums[i - 1])
            
		return res
