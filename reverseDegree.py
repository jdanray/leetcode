# https://leetcode.com/problems/reverse-degree-of-a-string/

class Solution(object):
	def reverseDegree(self, s):
		ab = string.ascii_lowercase
		val = {c: len(ab) - i for (i, c) in enumerate(ab)}
		return sum(val[c] * (i + 1) for i, c in enumerate(s))