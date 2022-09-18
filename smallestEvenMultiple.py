# https://leetcode.com/problems/smallest-even-multiple/ 

class Solution(object):
	def smallestEvenMultiple(self, n):
		return n * (n % 2 + 1)
