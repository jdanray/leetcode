# https://leetcode.com/problems/remove-zeros-in-decimal-representation/

class Solution(object):
	def removeZeros(self, n):
		p = 1
		res = 0
		while n > 0:
			d = n % 10
			if d != 0:
				res += p * d
				p *= 10
			n //= 10           
		return res