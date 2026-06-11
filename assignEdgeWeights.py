# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

class Solution(object):
	def assignEdgeWeights(self, edges):
		MOD = 10**9 + 7

		graph = collections.defaultdict(set)
		for (u, v) in edges:
			graph[u].add(v)
			graph[v].add(u)

		seen = {1}
		stack = [[1, 0]]
		m = 0
		while stack:
			u, d = stack.pop()

			m = max(m, d)

			for v in graph[u]:
				if v not in seen:
					seen.add(v)
					stack.append([v, d + 1])

		return pow(2, m - 1, MOD)
		return ((2 ** m) // 2) % MOD