# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/ 

class Solution(object):
	def numberOfSteps(self, num):
		s = 0
		while num > 0:
			if num % 2 == 1:
				num -= 1
			else:
				num //= 2
			s += 1

		return s
