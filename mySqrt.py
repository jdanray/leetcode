# https://leetcode.com/problems/sqrtx/ 

class Solution:
	def mySqrt(self, x):
		if x == 0 or x == 1:
			return x

		def condition(value):
			return value**2 > x

		left, right = 0, x
		while left < right:
			mid = left + (right - left) // 2

			if condition(mid):
				right = mid
			else:
				left = mid + 1

		return left - 1
