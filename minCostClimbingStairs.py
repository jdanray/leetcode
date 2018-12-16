# https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution(object):
	def minCostClimbingStairs(self, cost):
		memo = [0 for _ in range(len(cost))]
		memo[0] = cost[0]
		memo[1] = cost[1]
        
		for i in range(2, len(cost)):
			memo[i] = cost[i] + min(memo[i - 1], memo[i - 2])
            
		return min(memo[-1], memo[-2])

class Solution(object):
	def minCostClimbingStairs(self, cost):
		memo = {}

		def helper(i):
			if i >= len(cost):
				return 0

			if i not in memo:
				memo[i] = cost[i] + min(helper(i + 1), helper(i + 2))

			return memo[i]

		return min(helper(0), helper(1))
