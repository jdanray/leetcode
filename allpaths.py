# https://leetcode.com/problems/all-paths-from-source-to-target/description/

class Solution:
	def allPathsSourceTarget(self, graph):
		start = 0
		dest = len(graph) - 1
		stack = [[start]]
		paths = []
		while stack:
			p = stack.pop()
			if p[-1] == dest:
				paths.append(p)
				continue
			for child in graph[p[-1]]:
				stack.append(p + [child])
		return paths
