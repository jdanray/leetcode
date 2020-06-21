# https://leetcode.com/problems/course-schedule-iv/

class Solution(object):
	def checkIfPrerequisite(self, n, prerequisites, queries):
		graph = collections.defaultdict(set)
		for u, v in prerequisites:
			graph[u].add(v)

		prereqs = collections.defaultdict(set)
		def dfs(u):
			if u in prereqs:
				return prereqs[u]

			for v in graph[u]:
				prereqs[u].add(v)
				prereqs[u] |= dfs(v)
			return prereqs[u]

		for u in range(n):
			dfs(u)

		return [v in prereqs[u] for u, v in queries]
