# https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/ 

class Solution(object):
	def minCostToMoveChips(self, chips):
		N = len(chips)

		if N == 1:
			return 0

		res = float('inf')
		for dest in range(N):
			cost = 0
			for pos in chips:
				d = abs(pos - dest)
				if d % 2 == 1:
					cost += 1
			res = min(res, cost)

		return res
