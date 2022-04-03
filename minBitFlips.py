# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/ 

class Solution(object):
	def minBitFlips(self, start, goal):
		res = 0
		xor = start ^ goal
		while xor > 0:
			res += (xor & 1)
			xor >>= 1

		return res

class Solution(object):
	def minBitFlips(self, start, goal):
		res = 0
		while start > 0 or goal > 0:
			if start & 1 != goal & 1:
				res += 1

			start >>= 1
			goal >>= 1

		return res
