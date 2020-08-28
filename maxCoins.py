# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution(object):
	def maxCoins(self, piles):
		N = len(piles)
		piles = sorted(piles)
		s = 0
		i = N - 2
		for _ in range(N // 3):
			s += piles[i]
			i -= 2
		return s
