# https://leetcode.com/problems/maximal-network-rank/ 

class Solution(object):
	def maximalNetworkRank(self, n, roads):
		count = collections.Counter()
		connected = set()
		for (u, v) in roads:
			count[u] += 1
			count[v] += 1
			connected.add((min(x, y), max(x, y))

		res = 0
		for u in range(n):
			for v in range(u + 1, n):
				c = count[u] + count[v]
				if (u, v) in connected:
					c -= 1

				res = max(res, c)

		return res
