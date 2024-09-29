# https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/ 

class Solution(object):
	def minElement(self, nums):
		res = float('inf')
		for n in nums:
			s = 0
			while n > 0:
				s += n % 10
				n //= 10

			res = min(res, s)

		return res
