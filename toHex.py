# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/

class Solution:
	digs = '0123456789abcdef'
	def toHex(self, num):
		if num == 0:
			return '0'
		elif num < 0:
			num = (-num ^ 0xffffffff) + 1

		h = ''
		while num > 0:
			h = self.digs[num % 16] + h
			num //= 16
		return h
