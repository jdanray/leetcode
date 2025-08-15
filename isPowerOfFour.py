# https://leetcode.com/problems/power-of-four/

class Solution(object):
	def isPowerOfFour(self, n):
		def isPowerOf(b, n):
			if n <= 0:
				return False

			p = 1
			while p < n:
				p *= b

			return p == n

		return isPowerOf(4, n)

class Solution(object):
	def isPowerOfFour(self, n):
		r = -1
		b = 0
		while n > 0 and b == 0:
			b = n % 2
			r += 1
			n >>= 1

		return n == 0 and b == 1 and r % 2 == 0
