# https://leetcode.com/problems/count-integers-with-even-digit-sum/ 

class Solution(object):
	def countEven(self, num):
		res = 0
		for n in range(1, num + 1):
			s = 0
			while n > 0:
				d = n % 10
				s += d
				n //= 10

			if s % 2 == 0:
				res += 1

		return res
