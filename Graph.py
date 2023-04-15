# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/ 

class Graph(object):
	def __init__(self, n, edges):
		self.N = n
		self.graph = collections.defaultdict(set)
		for (u, v, w) in edges:
			self.graph[u].add((v, w))

	def addEdge(self, edge):
		u, v, w = edge
		self.graph[u].add((v, w))

	def shortestPath(self, node1, node2):
		dist = {u: float('inf') for u in range(self.N)}
		dist[node1] = 0

		pq = []
		heapq.heappush(pq, (dist[node1], node1))

		while pq:
			d, u = heapq.heappop(pq)

			if u == node2:
				return dist[node2]

			for (v, w) in self.graph[u]:
				if dist[v] > dist[u] + w:
					dist[v] = dist[u] + w
					heapq.heappush(pq, (dist[v], v))

		return -1
