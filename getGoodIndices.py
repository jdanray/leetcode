# https://leetcode.com/problems/double-modular-exponentiation/ 

class Solution(object):
	def getGoodIndices(self, variables, target):
		return [i for i, (a, b, c, m) in enumerate(variables) if ((a**b % 10)**c) % m == target]
