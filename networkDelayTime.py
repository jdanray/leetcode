# https://leetcode.com/problems/network-delay-time/

class Solution(object):
	def networkDelayTime(self, times, N, K):
		graph = [[] for _ in range(N + 1)]
		for (u, v, w) in times:
			graph[u].append([v, w])
	
		INFINITY = 10000
		dist = [INFINITY for _ in range(N + 1)]
		dist[K] = 0

		pq = []
		heapq.heappush(pq, (dist[K], K))
        
		while pq:
			_, u = heapq.heappop(pq)

			for (v, w) in graph[u]:
				if dist[v] > dist[u] + w:
					dist[v] = dist[u] + w
					heapq.heappush(pq, (dist[v], v))

		m = max(dist[1:])
		return -1 if m == INFINITY else m
