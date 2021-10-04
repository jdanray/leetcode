# https://leetcode.com/problems/minimum-moves-to-convert-string/

class Solution(object):
	def minimumMoves(self, s):
		res = 0
		i = 0
		while i < len(s):
			if s[i] == 'X':
				res += 1
				i += 3
			else:
				i += 1

		return res
