# https://leetcode.com/problems/smallest-string-with-swaps/

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
	def smallestStringWithSwaps(self, s, pairs):
		N = len(s)
		uf = DisjointSet(N)
		for (u, v) in pairs:
 			if uf.find(u) != uf.find(v):
				uf.union(u, v)

		groups = collections.defaultdict(list)
		for u in range(N):
			groups[uf.find(u)].append(u)

		res = [''] * N
		for rank in groups:
			g = groups[rank]
			chars = sorted(s[i] for i in g)
			for i in range(len(g)):
				res[g[i]] = chars[i]

		return ''.join(res)
