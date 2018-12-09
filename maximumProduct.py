# https://leetcode.com/problems/maximum-product-of-three-numbers/

class Solution:
	def maximumProduct(self, nums):
		nums = sorted(nums)
		return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
