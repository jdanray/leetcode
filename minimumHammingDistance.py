# https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/ 

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
	def minimumHammingDistance(self, source, target, allowedSwaps):
		uf = DisjointSet(len(source))
		for (i, j) in allowedSwaps:
			uf.union(i, j)

		count = collections.defaultdict(collections.Counter)
		for i, n in enumerate(source):
			f = uf.find(i)
			count[f][n] += 1

		res = 0
		for i, t in enumerate(target):
			f = uf.find(i)
			if count[f][t] == 0:
				res += 1
			else:
				count[f][t] -= 1

		return res
