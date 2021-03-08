# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/ 

class Solution(object):
	def checkPowersOfThree(self, n):
		p = 1
		while p * 3 <= n:
			p *= 3

		while p > 0 and n > 0:
			if n >= p:
				n -= p
			p //= 3

		return n == 0
