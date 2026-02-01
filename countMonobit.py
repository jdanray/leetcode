# https://leetcode.com/problems/count-monobit-integers/

class Solution(object):
	def countMonobit(self, n):
		b = 0
		res = 0
		while b <= n:
			b *= 2
			b += 1
			res += 1
		return res