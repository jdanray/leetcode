# https://leetcode.com/problems/find-if-path-exists-in-graph/ 

class Solution(object):
	def validPath(self, n, edges, start, end):
		graph = collections.defaultdict(set)
		for (u, v) in edges:
			graph[u].add(v)
			graph[v].add(u)
		
		queue = collections.deque([start])
		seen = set()
		while queue:
			u = queue.popleft()

			if u == end:
				return True

			for v in graph[u]:
				if v not in seen:
					queue.append(v)
					seen.add(v)

		return False
