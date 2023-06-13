# https://leetcode.com/problems/data-stream-as-disjoint-intervals/ 

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

class SummaryRanges(object):
	def __init__(self):
		self.nums = set()
		self.uf = DisjointSet(3 * 10 ** 4)

	def addNum(self, value):
		self.nums.add(value)

		if value - 1 in self.nums:
			self.uf.union(value - 1, value)

		if value + 1 in self.nums:
			self.uf.union(value + 1, value)

	def getIntervals(self):
		mini = {}
		maxi = {}
		for n in self.nums:
			f = self.uf.find(n)

			if f not in mini:
				mini[f] = n
			else:
				mini[f] = min(mini[f], n)

			if f not in maxi:
				maxi[f] = n
			else:
				maxi[f] = max(maxi[f], n)

		res = [[mini[f], maxi[f]] for f in mini]
		return sorted(res, key=lambda i: i[0])
