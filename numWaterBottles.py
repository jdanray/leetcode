# https://leetcode.com/problems/water-bottles/ 

class Solution(object):
	def numWaterBottles(self, numFull, numExchange):
		res = 0
		numEmpty = 0
		while numFull > 0:
			# drink
			res += numFull
			numEmpty += numFull

			# exchange
			numFull = numEmpty // numExchange
			numEmpty %= numExchange

		return res
