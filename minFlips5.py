# https://leetcode.com/problems/minimum-number-of-flips-to-reverse-binary-string/

class Solution(object):
	def minimumFlips(self, n):
		b = bin(n)[2:]
		r = b[::-1]
		return sum(r[i] != b[i] for i in range(len(b)))