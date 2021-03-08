# https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/ 

class Solution(object):
	def countRestrictedPaths(self, n, edges):
		MOD = 10 ** 9 + 7

		# build the graph

		graph = collections.defaultdict(list)
		for (u, v, w) in edges:
			graph[u].append((v, w))
			graph[v].append((u, w))

		# build distanceToLastNode
		# uses Dijkstra's algorithm

		dist = {}
		for u in graph:
			dist[u] = float('inf')
		dist[n] = 0

		pq = []
		heapq.heappush(pq, (dist[n], n))
		while pq:
			d, u = heapq.heappop(pq)

			if d != dist[u]:
				continue

			for (v, w) in graph[u]:
				if dist[u] + w < dist[v]:
					dist[v] = dist[u] + w
					heapq.heappush(pq, (dist[v], v))

		# find all restricted paths from 1 to n

		memo = {}
		def dfs(u):
			if u == n:
				return 1

			if u in memo:
				return memo[u]

			res = 0
			for (v, _) in graph[u]:
				if dist[u] > dist[v]:
					res += dfs(v)
			memo[u] = res
			return memo[u]

		return dfs(1) % MOD
