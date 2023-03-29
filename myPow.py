# https://leetcode.com/problems/powx-n/ 

class Solution(object):
 	def myPow(self, x, n):
		x = float(x)
        
		if n < 0:
			x = 1 / x
			n = abs(n)

		res = 1
		while n > 0:
			if n & 1 == 1:
				res *= x

			x *= x
			n >>= 1
            
		return res
