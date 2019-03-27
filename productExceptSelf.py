# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
	def productExceptSelf(self, nums):
		prod = []
		p = 1
		for n in nums:
			prod.append(p)
			p *= n

		p = 1
		for i in range(len(prod) - 1, -1, -1):
			prod[i] *= p
			p *= nums[i]

		return prod

