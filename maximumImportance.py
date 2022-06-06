# https://leetcode.com/problems/maximum-total-importance-of-roads/ 

class Solution(object):
	def maximumImportance(self, n, roads):
		count = collections.Counter()
		for (u, v) in roads:
			count[u] += 1
			count[v] += 1

		sort = sorted(count, key=lambda u: count[u], reverse=True)
		importance = {}
		for u in sort:
			importance[u] = n
			n -= 1

		res = 0
		for (u, v) in roads:
			res += importance[u] + importance[v]

		return res
