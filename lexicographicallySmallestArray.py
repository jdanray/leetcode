# https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/ 

from sortedcontainers import SortedList

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
	def lexicographicallySmallestArray(self, nums, limit):
		N = len(nums)

		elems = [(n, i) for i, n in enumerate(nums)]
		elems = sorted(elems)

		uf = DisjointSet(N)
		for i in range(N):
			if i - 1 >= 0 and elems[i][0] - elems[i - 1][0] <= limit:
				uf.union(elems[i][1], elems[i - 1][1])

		bins = collections.defaultdict(SortedList)
		for i, n in enumerate(nums):
			f = uf.find(i)
			bins[f].add(n)

		res = []
		for i, n in enumerate(nums):
			f = uf.find(i)
			x = bins[f].pop(0)
			res.append(x)

		return res
