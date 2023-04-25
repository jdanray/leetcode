# https://leetcode.com/problems/sum-multiples/ 

class Solution(object):
	def sumOfMultiples(self, n):
		return sum(u for u in range(1, n + 1) if any(u % m == 0 for m in [3,5,7]))
