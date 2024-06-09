# https://leetcode.com/problems/clear-digits/ 

class Solution(object):
	def clearDigits(self, s):
		res = []
		for c in s:
			if c.isnumeric():
				res.pop()
			else:
				res.append(c)

		return ''.join(res)
