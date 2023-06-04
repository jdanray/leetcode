# https://leetcode.com/problems/find-circles/

class Solution:
	def findCircleNum(self, M):
		N = len(M)
		seen = set()

		def dfs(i):
			seen.add(i)
			for j in range(N):
				if M[i][j] == 1 and j not in seen:
					dfs(j)

		ncircles = 0
		for i in range(N):
			if i not in seen:
				dfs(i)
				ncircles += 1

		return ncircles

# union-find solution 

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
	def findCircleNum(self, isConnected):
		N = len(isConnected)

		uf = DisjointSet(N)
		for u in range(N):
			for v in range(N):
				if isConnected[u][v]:
					uf.union(u, v)

		return len(set(uf.find(u) for u in range(N)))
