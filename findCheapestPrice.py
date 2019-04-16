class Solution(object):
	def findCheapestPrice(self, n, flights, src, dst, K):
		graph = {}
		for (u, v, cost) in flights:
			if u not in graph:
				graph[u] = []
			graph[u].append([v, cost])

		pq = [[0, src, 0]]
		while pq:
			cost, u, k = heapq.heappop(pq)

			if u == dst:
				return cost

			if u not in graph:
				continue

			if u != src:
				k += 1

			if k > K:
				continue

			for (v, c) in graph[u]:
				heapq.heappush(pq, [cost + c, v, k])

		return -1
