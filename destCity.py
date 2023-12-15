# https://leetcode.com/problems/destination-city/

class Solution(object):
	def destCity(self, paths):
		cities = set()
		for (u, v) in paths:
			cities.add(u)
			cities.add(v)

		outgoing = set(u for u, _ in paths)

		return list(cities - outgoing)[0]

class Solution(object):
	def destCity(self, paths):
		graph = collections.defaultdict(str)
		for (u, v) in paths:
			graph[u] = v

		u = paths[0][0]
		while u in graph:
			u = graph[u]

		return u

class Solution(object):
	def destCity(self, paths):
		cands = collections.defaultdict(bool)
		for (a, b) in paths:
			cands[a] = False
			if b not in cands:
				cands[b] = True

		for c in cands:
			if cands[c]:
				return c

class Solution(object):
	def destCity(self, paths):
		for (_, b) in paths:
			if not any(b == c for (c, _) in paths):
				return b
