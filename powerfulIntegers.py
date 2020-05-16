# https://leetcode.com/problems/powerful-integers/

class Solution(object):
	def powerfulIntegers(self, x, y, bound):
		res = set()
		xpow = 1
		while xpow < bound:
			ypow = 1
			while xpow + ypow <= bound:
				res.add(xpow + ypow)
				if y == 1:
					break
				ypow *= y

			if x == 1:
				break
			xpow *= x
            
		return list(res)
