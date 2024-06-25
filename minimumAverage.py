# https://leetcode.com/problems/minimum-average-of-smallest-and-largest-elements/ 

class Solution(object):
	def minimumAverage(self, nums):
		nums = sorted(nums)
		i = 0
		j = len(nums) - 1
		res = float('inf')
		while i < j:
			res = min(res, (1.0 * nums[i] + nums[j]) / 2)
			i += 1
			j -= 1
            
		return res
