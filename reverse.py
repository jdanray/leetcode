# https://leetcode.com/problems/reverse-integer/

class Solution(object):
	def reverse(self, x):
		neg = False
		if x < 0:
			neg = True
			x = -x

		p = -1
		y = x
		while y > 0:
			p += 1
			y //= 10
	
		p = 10 ** p
		r = 0
		while x > 0:
			d = x % 10
			r += (d * p)
			p //= 10
			x //= 10

		if neg:
			r = -r

		lim = 2 ** 31
		if r < -lim or r > lim - 1:
			return 0
		else:
			return r
