# https://leetcode.com/problems/harshad-number/ 

class Solution(object):
	def sumOfTheDigitsOfHarshadNumber(self, x):
		n = x
		s = 0
		while n > 0:
			s += n % 10
			n //= 10

		return s if x % s == 0 else -1
