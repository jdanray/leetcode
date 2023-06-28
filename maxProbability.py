# https://leetcode.com/problems/path-with-maximum-probability/ 

class Solution(object):
	def maxProbability(self, n, edges, succProb, start, end):
		graph = collections.defaultdict(set)
		for i, (u, v) in enumerate(edges):
			graph[u].add((v, succProb[i]))
			graph[v].add((u, succProb[i]))

		dist = {}
		for u in graph:
			dist[u] = 0.0
		dist[start] = 1.0

		pq = [(-dist[start], start)]
		heapq.heapify(pq)

		while pq:
			_, u = heapq.heappop(pq)

			if u == end:
				return dist[end]

			for (v, w) in graph[u]:
				if dist[v] < dist[u] * w:
					dist[v] = dist[u] * w
					heapq.heappush(pq, (-dist[v], v))

		return 0.0
