# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/ 

class Solution(object):
	def maxProduct(self, nums):
		nums = sorted(nums)
		return (nums[-1] - 1) * (nums[-2] - 1)
