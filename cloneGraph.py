# https://leetcode.com/problems/clone-graph/ 

class Solution(object):
	def cloneGraph(self, node):
		if not node:
			return None

		stack = [node]
		seen = {}
		while stack:
			u = stack.pop()

			seen[u] = Node(u.val)

			for v in u.neighbors:
				if v not in seen:
					stack.append(v)

		for u in seen:
			for v in u.neighbors:
				seen[u].neighbors.append(seen[v])

		return seen[node]
