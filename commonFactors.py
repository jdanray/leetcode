# https://leetcode.com/problems/number-of-common-factors/ 

class Solution(object):
	def commonFactors(self, a, b):
		return sum(1 if a % f == 0 and b % f == 0 else 0 for f in range(1, min(a, b) + 1))	
