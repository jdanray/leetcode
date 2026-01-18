# https://leetcode.com/problems/maximum-capacity-within-budget/

class Solution(object):
	def maxCapacity(self, costs, capacity, budget):
		maxCap = []
		costCap = sorted(zip(costs, capacity))
		res = float('-inf')
		for (cost, cap) in costCap:
			while maxCap and cost + maxCap[0][1] >= budget:
				heapq.heappop(maxCap)

			if maxCap:
				res = max(res, cap - maxCap[0][0])
			elif cost < budget:
				res = max(res, cap)

			heapq.heappush(maxCap, (-cap, cost))

		return res if res != float('-inf') else 0