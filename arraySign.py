# https://leetcode.com/problems/sign-of-the-product-of-an-array/ 

class Solution(object):
	def arraySign(self, nums):
		res = 1
		for n in nums:
			if n == 0:
				return 0
			elif n < 0:
				res = -res
		return res
