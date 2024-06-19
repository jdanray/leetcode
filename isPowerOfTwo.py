# https://leetcode.com/problems/power-of-two/

class Solution(object):
	def isPowerOfTwo(self, n):
		p = 1
		while p <= n:
			if p == n:
				return True
			p *= 2

		return False

class Solution(object):
	def isPowerOfTwo(self, n):
		if n <= 0:
			return False

		c = 0
		while n > 0:
			if n & 1 == 1:
				c += 1

			if c > 1:
				return False

			n >>= 1

		return c == 1

"""
The problem statement also challenges you to solve the problem without loops/recursions. 

I found the bit operations here: https://stackoverflow.com/questions/8871204/count-number-of-1s-in-binary-representation/17498333#17498333

I wrote the solution in Python:
"""

class Solution(object):
	def isPowerOfTwo(self, n):
		if n <= 0:
			return False

		n = (n & 0x55555555) + ((n >> 1) & 0x55555555)
		n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
		n = (n & 0x0f0f0f0f) + ((n >> 4) & 0x0f0f0f0f)
		n = (n & 0x00ff00ff) + ((n >> 8) & 0x00ff00ff)
		n = (n & 0x0000ffff) + ((n >> 16) & 0x0000ffff)

		return n == 1
