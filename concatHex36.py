# https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/

class Solution(object):
	def concatHex36(self, n):
		def toBase(n, base):
			if n == 0:
				return '0'

			res = ''
			while n > 0:
				d = n % base
				if d >= 10:
					res += string.ascii_uppercase[d - 10]
				else:
					res += str(d)
				n //= base
			return res[::-1]

		return toBase(n ** 2, 16) + toBase(n ** 3, 36)