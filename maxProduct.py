# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/ 

class Solution(object):
	def maxProduct(self, nums):
		m1 = 0
		m2 = 0
		for n in nums:
			if n > m1:
				m1, m2 = n, m1
			elif n > m2:
				m2 = n

		return (m1 - 1) * (m2 - 1)

class Solution(object):
	def maxProduct(self, nums):
		nums = sorted(nums)
		return (nums[-1] - 1) * (nums[-2] - 1)
