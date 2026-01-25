# https://leetcode.com/problems/pythagorean-distance-nodes-in-a-tree/

class Solution(object):
	def specialNodes(self, n, edges, x, y, z):
		tree = collections.defaultdict(set)
		for (u, v) in edges:
			tree[u].add(v)
			tree[v].add(u)

		dist = collections.defaultdict(int)
		def getDist(start):
			seen = {start}
			stack = [[start, 0]]
			while stack:
				u, d = stack.pop()

				dist[u, start] = d

				for v in tree[u]:
					if v not in seen:
						seen.add(v)
						stack.append([v, d + 1])

		getDist(x)
		getDist(y)
		getDist(z)

		res = 0
		for u in range(n):
			a, b, c = sorted([dist[u, x], dist[u, y], dist[u, z]])
			if a**2 + b**2 == c**2:
				res += 1
		return res