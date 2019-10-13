# https://leetcode.com/problems/split-a-string-in-balanced-strings/ 

class Solution(object):
	def balancedStringSplit(self, s):
		offset = 0
		res = 0
		for c in s:
			if c == 'L':
				offset += 1
			elif c == 'R':
				offset -= 1

			if offset == 0:
				res += 1

		return res
