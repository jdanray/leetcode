# https://leetcode.com/problems/perfect-number/

from math import sqrt

class Solution:
	def checkPerfectNumber(self, num):
		if num < 2:
			return False

		i = 2
		s = 0
		while i <= sqrt(num):
			if num % i == 0:
				s += i + num // i
			i += 1

		return s == num - 1
