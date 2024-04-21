# https://leetcode.com/problems/find-if-path-exists-in-graph/ 

class Solution(object):
	def validPath(self, n, edges, start, end):
		graph = collections.defaultdict(set)
		for (u, v) in edges:
			graph[u].add(v)
			graph[v].add(u)
		
		queue = collections.deque([start])
		seen = set()
		while queue:
			u = queue.popleft()

			if u == end:
				return True

			for v in graph[u]:
				if v not in seen:
					queue.append(v)
					seen.add(v)

		return False

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
	def validPath(self, n, edges, source, destination):
		uf = DisjointSet(n)
		for (u, v) in edges:
			uf.union(u, v)

		return uf.find(source) == uf.find(destination)
