# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/ 

class Solution(object):
	def minReorder(self, n, connections):
		inedges = collections.defaultdict(set)
		outedges = collections.defaultdict(set)
		for (u, v) in connections:
			inedges[v].add(u)
			outedges[u].add(v)

		stack = [0]
		seen = {0}
		res = 0
		while stack:
			u = stack.pop()

			for v in outedges[u]:
				if v not in seen:
					res += 1
					stack.append(v)
					seen.add(v)

			for v in inedges[u]:
				if v not in seen:
					stack.append(v)
					seen.add(v)

		return res
