# https://leetcode.com/problems/water-bottles-ii/ 

class Solution(object):
	def maxBottlesDrunk(self, numBottles, numExchange):
		numEmpty = 0
		res = 0
		while numBottles > 0:
			# drink
			numEmpty += numBottles
			res += numBottles
			numBottles = 0

			# exchange
			if numEmpty >= numExchange:
				numEmpty -= numExchange
				numBottles = 1
				numExchange += 1

		return res
