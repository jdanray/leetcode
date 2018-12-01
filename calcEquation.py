# https://leetcode.com/problems/evaluate-division/

class Solution:
	def calcEquation(self, equations, values, queries):
		def dfs(s, t):
			visited = set()
			stack = [[s, 1.0]]
			while stack:
				u, w = stack.pop()

				if u not in graph:
					continue

				if u == t:
					return w

				for v in graph[u]:
					if v not in visited:
						stack.append([v, graph[u][v] * w])
						visited.add(v)
			return -1.0
		
		graph = dict()
		for i in range(len(equations)):
			u, v = equations[i]
			w = values[i]

			if u not in graph:
				graph[u] = dict()
			if v not in graph:
				graph[v] = dict()

			graph[u][v] = w
			graph[v][u] = 1 / w

		return [dfs(s, t) for s, t in queries]
