# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

class Solution(object):
	def minFlips(self, a, b, c):
		n = 0
		while a > 0 or b > 0 or c > 0:
			bita = a & 1
			bitb = b & 1
			bitc = c & 1

			if bitc == 0:
				if bita == 1 and bitb == 1:
					n += 2
				elif bita == 1 or bitb == 1:
					n += 1
			elif bitc == 1:
				if bita == 0 and bitb == 0:
					n += 1

			a >>= 1
			b >>= 1
			c >>= 1

		return n
