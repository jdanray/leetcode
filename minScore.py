# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

class Solution(object):
	def minScore(self, n, roads):
		graph = collections.defaultdict(list)
		for (u, v, w) in roads:
			graph[u].append([v, w])
			graph[v].append([u, w])

		res = float('inf')
		stack = [1]
		seen = set()
		while stack:
			u = stack.pop(0)

			for (v, w) in graph[u]:
				res = min(res, w)
				if v not in seen:
					stack.append(v)
					seen.add(v)

		return res 
