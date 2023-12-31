# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/ 

class Solution(object):
	def largestPerimeter(self, nums):
		nums = sorted(nums, reverse=True)
		p = sum(nums)
		for n in nums:
			if p - n > n:
				return p
			p -= n
		return -1
