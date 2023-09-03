# https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/ 

class Solution(object):
	def minCost(self, startPos, homePos, rowCosts, colCosts):
		res = 0
		if startPos[0] >= homePos[0]:
			for i in range(startPos[0] - 1, homePos[0] - 1, -1):
				res += rowCosts[i]
		else:
			for i in range(startPos[0] + 1, homePos[0] + 1):
				res += rowCosts[i]

		if startPos[1] >= homePos[1]:
			for j in range(startPos[1] - 1, homePos[1] - 1, -1):
				res += colCosts[j]
		else:
			for j in range(startPos[1] + 1, homePos[1] + 1):
				res += colCosts[j]

		return res
