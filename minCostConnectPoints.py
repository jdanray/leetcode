# https://leetcode.com/problems/min-cost-to-connect-all-points/

class DisjointSet:
	def __init__(self, N):
		self.id = range(N)
		self.rank = [1] * N

	def find(self, x):
		if self.id[x] != self.id[self.id[x]]:
			self.id[x] = self.find(self.id[x])
		return self.id[x]

	def union(self, x, y):
		xx = self.find(x)
		yy = self.find(y)
		if xx == yy:
			return False
		elif self.rank[xx] > self.rank[yy]:
			xx, yy = yy, xx
		elif self.rank[xx] == self.rank[yy]:
			self.rank[yy] += 1
		self.id[xx] = yy
		return True

class Solution(object):
	def minCostConnectPoints(self, points):
		N = len(points)

		pq = []
		heapq.heapify(pq)
		for i, u in enumerate(points):
			for j, v in enumerate(points):
				if i != j:
					d = abs(u[0] - v[0]) + abs(u[1] - v[1])
					heapq.heappush(pq, (d, i, j))

		uf = DisjointSet(N)
		connected = 0
		res = 0
		while pq:
			d, i, j = heapq.heappop(pq)

			if uf.union(i, j):
				res += d
				connected += 1

			if connected == N - 1:
				break

		return res
