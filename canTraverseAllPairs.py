# https://leetcode.com/problems/greatest-common-divisor-traversal/ 

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
	def canTraverseAllPairs(self, nums):
		N = len(nums)

		mx = max(nums) + 1
		sieve = list(range(mx))
		for n in range(4, mx, 2):
			sieve[n] = 2
		for n in range(3, int(math.ceil(math.sqrt(mx)))):
			if sieve[n] != n:
				continue
			for k in range(n * n, mx, n):
				if sieve[k] == k:
					sieve[k] = n

		uf = DisjointSet(N)
		seen = {}
		for i, n in enumerate(nums):
				while n != 1:
					f = sieve[n]
					if f in seen:
						uf.union(i, seen[f])
					else:
						seen[f] = i
					n //= f

		return len(set(uf.find(i) for i in range(N))) == 1
