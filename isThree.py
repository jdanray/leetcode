# https://leetcode.com/problems/three-divisors/

class Solution(object):
	def isThree(self, n):
		N = 3
		d = 0
		for x in range(1, n + 1):
			if n % x == 0:
				d += 1
                
		return d == N
