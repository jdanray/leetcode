# https://leetcode.com/problems/hamming-distance/description/

class Solution:
	def hammingDistance(self, x, y):
		d = 0
		for i in range(32):
			bx = x & (1 << i)
			by = y & (1 << i)
			if bx != by:
				d += 1
		return d

class Solution:
	def hammingDistance(self, x, y):
		d = 0
		for _ in range(32):
			d += (x & 1) ^ (y & 1)
			x >>= 1
			y >>= 1
		return d
