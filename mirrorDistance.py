# https://leetcode.com/problems/mirror-distance-of-an-integer/

class Solution(object):
	def mirrorDistance(self, n):
		def reverse(n):
			r = 0
			while n > 0:
				r *= 10
				r += n % 10
				n //= 10
			return r

		return abs(n - reverse(n))