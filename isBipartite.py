# https://leetcode.com/problems/is-graph-bipartite/

class Solution:
	def isBipartite(self, graph):
		colors = [0 for _ in range(len(graph))]
        
		def dfs(u, col):
			if colors[u] != 0: 
				return colors[u] == col

			colors[u] = col
			return all(dfs(v, -col) for v in graph[u])

		return all(colors[u] != 0 or dfs(u, 1) for u in range(len(graph))) 
