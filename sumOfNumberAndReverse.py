# https://leetcode.com/problems/sum-of-number-and-its-reverse/ 

class Solution(object):
	def sumOfNumberAndReverse(self, num):
		for n in range(num + 1):
			r = 0
			m = n
			while m > 0:
				r *= 10
				r += (m % 10)
				m //= 10

			if n + r == num:
				return True

		return False
