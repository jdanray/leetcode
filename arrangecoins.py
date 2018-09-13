# https://leetcode.com/problems/arranging-coins/description/

class Solution(object):
	def arrangeCoins(self, n):
		k = 0
		while n > 0:
			k += 1
			n -= k

		if n < 0: 
			k -= 1

		return k
