# https://leetcode.com/problems/find-champion-ii/

class Solution(object):
	def findChampion(self, n, edges):
		graph = collections.defaultdict(set)
		for (u, v) in edges:
			graph[u].add(v)

		seen = set()
		def dfs(u):
			for v in graph[u]:
				if v not in seen:
					seen.add(v)
					dfs(v)

		for u in range(n):
			if u in seen:
				continue

			for v in graph[u]:
				dfs(u)

		cands = set(range(n)) - seen 
		if len(cands) == 1:
			return next(iter(cands))
		else:
			return -1
