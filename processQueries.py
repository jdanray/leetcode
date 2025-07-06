# https://leetcode.com/problems/power-grid-maintenance/

class DisjointSet:
	def __init__(self, N):
		self.id = list(range(N))
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
		if self.rank[xx] > self.rank[yy]:
			xx, yy = yy, xx
		if self.rank[xx] == self.rank[yy]:
			self.rank[yy] += 1

		self.id[xx] = yy
		return True

class Solution(object):
	def processQueries(self, c, connections, queries):
		uf = DisjointSet(c + 1)
		for (u, v) in connections:
			uf.union(u, v)

		nodes = collections.defaultdict(list)
		idx = collections.defaultdict(int)
		online = collections.defaultdict(bool)
		for u in range(1, c + 1):
			id = uf.find(u)
			nodes[id].append(u)
			idx[id] = 0
			online[u] = True

		res = []
		for (t, u) in queries:
			if t == 1:
				if online[u]:
					res.append(u)
					continue

				id = uf.find(u)
				while idx[id] < len(nodes[id]) and not online[nodes[id][idx[id]]]:
					idx[id] += 1

				if idx[id] >= len(nodes[id]):
					res.append(-1)
				else:
					res.append(nodes[id][idx[id]])

			if t == 2:
				online[u] = False

		return res