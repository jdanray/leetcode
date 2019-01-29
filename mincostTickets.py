# https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution(object):
	def mincostTickets(self, days, costs):
		def consec(d, n):
			k = d + 1
			while k < len(days) and days[k] - days[d] < n:
				k += 1
			return k

		memo = {}
		def mincost(d):
			if d >= len(days):
				return 0

			if d not in memo:
				a = costs[0] + mincost(d + 1)
				b = costs[1] + mincost(consec(d, 7))
				c = costs[2] + mincost(consec(d, 30))
				memo[d] = min(a, b, c)
			return memo[d]

		return mincost(0)
