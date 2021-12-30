# https://leetcode.com/problems/number-of-operations-to-make-network-connected/ 

class Solution(object):
	def makeConnected(self, n, connections):
		if len(connections) < n - 1:
			return -1

		graph = collections.defaultdict(set)
		for (u, v) in connections:
			graph[u].add(v)
			graph[v].add(u)

		seen = set()
		def dfs(u):
			seen.add(u)
            
			for v in graph[u]:
				if v not in seen:
					dfs(v)

		components = 0
		for u in range(n):
			if u not in seen:
				dfs(u)
				components += 1

		return components - 1
