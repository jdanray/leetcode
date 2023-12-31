# https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/ 

class Solution(object):
	def hasTrailingZeros(self, nums):
		zero = False
		for n in nums:
			if n % 2 == 0:
				if zero:
					return True
				else:
					zero = True
		return False
