# https://leetcode.com/problems/reachable-nodes-with-restrictions/ 

class Solution(object):
	def reachableNodes(self, n, edges, restricted):
		restricted = set(restricted)

		graph = collections.defaultdict(set)
		for (u, v) in edges:
			graph[u].add(v)
			graph[v].add(u)

		seen = set()
		stack = [0]
		while stack:
			u = stack.pop()
			seen.add(u)

			for v in graph[u]:
				if v not in restricted and v not in seen:
					stack.append(v)

		return len(seen)
