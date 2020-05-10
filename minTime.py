#  https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

class Solution(object):
	def minTime(self, n, edges, hasApple):
		graph = collections.defaultdict(set)
		for (u, v) in edges:
			graph[u].add(v)
			graph[v].add(u)

		visited = set()
		def dfs(u):
			if u in visited:
				return 0
			
			visited.add(u)
			res = sum(dfs(v) for v in graph[u])
			if (res > 0 or hasApple[u]) and u != 0:
				res += 2
			return res

		return dfs(0)
