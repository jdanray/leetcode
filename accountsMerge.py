# https://leetcode.com/problems/accounts-merge/ 

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
	def accountsMerge(self, accounts):
		uf = DisjointSet(len(accounts))
		seen = dict()
		for i, a in enumerate(accounts):
			for e in a[1:]:
				if e in seen:
					uf.union(seen[e], i)
				else:
					seen[e] = i

		emails = collections.defaultdict(set)
		for i, a in enumerate(accounts):
			f = uf.find(i)
			for e in a[1:]:
				emails[f].add(e)

		res = []
		for f in emails:
			res.append([accounts[f][0]])
			res[-1] += sorted(emails[f])

		return res
