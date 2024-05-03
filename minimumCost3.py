# https://leetcode.com/problems/minimum-cost-to-convert-string-i/ 

# Floyd-Warshall
class Solution(object):
	def minimumCost(self, source, target, original, changed, cost):
		dist = {(u, v): float('inf') for u in string.ascii_lowercase for v in string.ascii_lowercase}
		for (u, v, w) in zip(original, changed, cost):
			dist[u, v] = min(dist[u, v], w)

		for k in string.ascii_lowercase:
			for i in string.ascii_lowercase:
				for j in string.ascii_lowercase:
					dist[i, j] = min(dist[i, j], dist[i, k] + dist[k, j])

		res = 0
		for (s, t) in zip(source, target):
			if s == t:
				continue

			if dist[s, t] == float('inf'):
				return -1

			res += dist[s, t]

		return res 

# Dijkstra
class Solution(object):
	def minimumCost(self, source, target, original, changed, cost):
		graph = collections.defaultdict(set)
		for (u, v, w) in zip(original, changed, cost):
			graph[u].add((v, w))

		dist = collections.defaultdict(int)
		def dijkstra(s):
			for u in string.ascii_lowercase:
				dist[s, u] = float('inf')
			dist[s, s] = 0 

			pq = [(dist[s, s], s)]
			heapq.heapify(pq)
			while pq:
				_, u = heapq.heappop(pq)
				for (v, w) in graph[u]:
					if dist[s, v] > dist[s, u] + w:
						dist[s, v] = dist[s, u] + w
						heapq.heappush(pq, (dist[s, v], v))

		for u in string.ascii_lowercase:
			dijkstra(u)

		res = 0
		for (s, t) in zip(source, target):
			if (s, t) not in dist or dist[s, t] == float('inf'):
				return -1
			else:
				res += dist[s, t]
		return res
