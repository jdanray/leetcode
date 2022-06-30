# https://leetcode.com/problems/count-asterisks/ 

class Solution(object):
	def countAsterisks(self, s):
		res = 0
		b = 0
		for c in s:
			if c == '|':
				b += 1
			elif c == '*' and b % 2 == 0:
				res += 1

		return res
