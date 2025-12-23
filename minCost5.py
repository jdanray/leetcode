# https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

class Solution(object):
	def minCost(self, s, cost):
		cc = collections.defaultdict(int)
		for i, c in enumerate(s):
			cc[c] += cost[i]

		total = sum(cost)
		return min(total - cc[c] for c in s)