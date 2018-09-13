# https://leetcode.com/problems/string-compression/description/

class Solution(object):
	def compress(self, chars):
		l = 0
		i = 0
		while i < len(chars):
			n = 1
			while i + 1 < len(chars) and chars[i] == chars[i + 1]:
				n += 1
				i += 1

			d = chars[i]
			if n > 1:
				d += str(n)

			for c in d:
				chars[l] = c
				l += 1
			i += 1
		return l
