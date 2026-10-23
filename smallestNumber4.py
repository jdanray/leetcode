# https://leetcode.com/problems/smallest-number-with-all-set-bits/

class Solution(object):
	def smallestNumber(self, n):
		i = 0
		res = 0
		while res < n:
			res += (1 << i)
			i += 1
            
		return res