# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/ 

class Solution(object):
	def getAncestors(self, n, edges):
		graph = collections.defaultdict(set)
		for (u, v) in edges:
			graph[v].add(u)

		res = [set() for _ in range(n)]
		memo = {}
		def dfs(u):
			if u in memo:
				return memo[u] 

			for v in graph[u]:
				res[u].add(v)
				res[u] |= dfs(v)

			memo[u] = res[u]
			return res[u]

		for u in range(n):
			dfs(u)

		return [sorted(r) for r in res]
