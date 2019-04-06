# https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
	def judgeSquareSum(self, c):
		a = 0
		b = int(c ** (1/2))
		while a <= b:
			d = a ** 2 + b ** 2
			if d < c:
				a += 1
			elif d > c:
				b -= 1
			else:
				return True

		return False
