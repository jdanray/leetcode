# https://leetcode.com/problems/redundant-connection/

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
	def findRedundantConnection(self, edges):
		uf = DisjointSet(len(edges))
		for e in edges:
			if not uf.union(e[0] - 1, e[1] - 1):
				return e
