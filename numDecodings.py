# https://leetcode.com/problems/decode-ways/

class Solution(object):
	def numDecodings(self, s):
		n1 = 1
		n2 = 1
		for i in range(len(s) - 1, -1, -1):
			if s[i] == '0':
				n = 0
			else:
				n = n1

			if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] <= '6')):
				n += n2

			n1, n2 = n, n1

		return n1
