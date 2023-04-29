# https://leetcode.com/problems/similar-string-groups/ 

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
	def numSimilarGroups(self, strs):
		N = len(strs)

		def similar(a, b):
			n = 0
			for i in range(len(a)):
				if a[i] != b[i]:
					n += 1
					if n > 2:
						return False
			return True

		uf = DisjointSet(N) 
		for i in range(N):
			for j in range(i + 1, N):
				if similar(strs[i], strs[j]):
					uf.union(i, j)

		return len(set(uf.find(i) for i in range(N)))
