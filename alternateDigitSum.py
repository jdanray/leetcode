# https://leetcode.com/problems/alternating-digit-sum/ 

class Solution(object):
	def alternateDigitSum(self, n):
		digs = []
		while n > 0:
			d = n % 10
			digs = [d] + digs
			n //= 10

		res = 0
		sign = 1
		for d in digs:
			res += sign * d
			sign = -sign

		return res

class Solution(object):
	def alternateDigitSum(self, n):
		sums = [0, 0]
		i = 0
		while n > 0:
			d = n % 10
			sums[i] += d
			i = 1 - i
			n //= 10

		sums[i] = -sums[i]
		return sums[0] + sums[1]
