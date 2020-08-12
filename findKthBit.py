# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution(object):
	def findKthBit(self, n, k):
		def genS(n):
			if n == 1:
				return '0'

			prev = genS(n - 1)
			invert = ''
			for p in prev:
				if p == '0':
					invert += '1'
				else:
					invert += '0'

			return prev + '1' + invert[::-1]

		return genS(n)[k - 1]
