# https://leetcode.com/problems/unit-conversion-i/

class Solution(object):
	def baseUnitConversions(self, conversions):
		MOD = 10**9 + 7

		graph = collections.defaultdict(set)
		for (u, v, f) in conversions:
			graph[u].add((v, f))

		stack = [[0, 1]]
		res = [0 for _ in range(len(conversions) + 1)]
		while stack:
			u, c = stack.pop()

			res[u] = c

			for (v, f) in graph[u]:
				stack.append([v, (c * f) % MOD])

		return res