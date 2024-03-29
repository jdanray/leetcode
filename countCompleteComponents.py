# https://leetcode.com/problems/count-the-number-of-complete-components/ 

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
		if self.rank[xx] > self.rank[yy]:
			xx, yy = yy, xx
		if self.rank[xx] == self.rank[yy]:
			self.rank[yy] += 1
		self.id[xx] = yy
		return True

class Solution(object):
	def countCompleteComponents(self, n, edges):
		numEdges = collections.Counter()
		uf = DisjointSet(n)
		for (u, v) in edges:
			numEdges[u] += 1
			numEdges[v] += 1
			uf.union(u, v)

		comps = collections.defaultdict(set)
		for u in range(n):
			comps[uf.find(u)].add(u)

		res = 0
		for c in comps:
			if all(numEdges[u] == len(comps[c]) - 1 for u in comps[c]):
				res += 1

		return res
