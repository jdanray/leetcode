# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

charToInt = {c: i for i, c in enumerate(ascii_lowercase)}

class DisjointSet:
	def __init__(self, N):
		self.id = list(range(N))
		self.rank = [1] * N
	
	def find(self, x):
		if not isinstance(x, int):
			x = charToInt[x]

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
	def smallestEquivalentString(self, a, b, s):
		uf = DisjointSet(len(ascii_lowercase))
		for i in range(len(a)):
			uf.union(a[i], b[i])

		smallest = {}
		for c in ascii_lowercase:
			id = uf.find(c)
			if id not in smallest or smallest[id] > c:
				smallest[id] = c

		return ''.join(smallest[uf.find(c)] for c in s)
