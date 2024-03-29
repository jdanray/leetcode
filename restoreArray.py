# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

class Solution(object):
	def restoreArray(self, adjacentPairs):
		graph = collections.defaultdict(set)
		for (u, v) in adjacentPairs:
			graph[u].add(v)
			graph[v].add(u)

		for u in graph:
			if len(graph[u]) == 1:
				stack = [u]
				seen = {u}
				break

		res = []
		while stack:
			u = stack.pop()

			res.append(u)

			for v in graph[u]:
				if v not in seen:
					stack.append(v)
					seen.add(v)

		return res

class Solution(object):
	def restoreArray(self, adjacentPairs):
		graph = collections.defaultdict(list)
		for (u, v) in adjacentPairs:
			graph[u].append(v)
			graph[v].append(u)

		path = []
		used = set()
		stack = []
		for u in graph:
			if len(graph[u]) == 1:
				path = [u]
				used = {u}
				stack = [graph[u][0]]
				break

		while stack:
			v = stack.pop()
			path += [v]

			if len(graph[v]) == 1 or (graph[v][0] in used and graph[v][1] in used):
				break

			used.add(v)
			if graph[v][0] in used:
				stack.append(graph[v][1])
			else:
				stack.append(graph[v][0])

		return path
