# https://leetcode.com/problems/maximum-profit-of-operating-a-centennial-wheel/

class Solution(object):
	def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
		gondolaSize = 4
		waiting = 0
		boarded = 0
		maxProfit = -1
		maxProfRot = 0
		rot = 0
		i = 0
		while i < len(customers) or waiting > 0:
			if i < len(customers):
				waiting += customers[i]
				i += 1

			b = min(gondolaSize, waiting)
			waiting -= b
			boarded += b

			rot += 1
			profit = (boarded * boardingCost) - (rot * runningCost)
			if profit > maxProfit:
				maxProfit = profit
				maxProfRot = rot

		return maxProfRot if maxProfit > 0 else -1 
