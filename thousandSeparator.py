# https://leetcode.com/problems/thousand-separator/

class Solution(object):
	def thousandSeparator(self, n):
		if n == 0:
			return '0'

		t = 0
		res = ''
		while n > 0:
			if t != 0 and t % 3 == 0:
				res = '.' + res

			d = n % 10
			res = str(d) + res

			t += 1
			n //= 10
		return res
