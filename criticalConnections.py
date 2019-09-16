# https://leetcode.com/problems/critical-connections-in-a-network/ 

# apply Tarjan's bridge-finding algorithm

class Solution(object):
	def criticalConnections(self, n, connections):
		self.time = 0
		disc = [float('inf') for _ in range(n)] 
		low = [float('inf') for _ in range(n)]
		parent = [-1 for _ in range(n)]
		res = []

		graph = collections.defaultdict(set)
		for u, v in connections:
			graph[u].add(v)
			graph[v].add(u)

		def dfs(u):
			disc[u] = self.time
			low[u] = self.time
			self.time += 1

			for v in graph[u]:
				if parent[v] == -1:
					parent[v] = u
					dfs(v)
					low[u] = min(low[u], low[v])
					if low[v] > disc[u]:
						res.append([u, v]) 
				elif v != parent[u]:
					low[u] = min(low[u], disc[v])

		for u in range(n): 
			if parent[u] == -1: 
				dfs(u)

		return res 
