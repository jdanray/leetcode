# https://leetcode.com/problems/flower-planting-with-no-adjacent/

# Somewhat simpler solution than the following one
class Solution(object):
	def gardenNoAdj(self, N, paths):
		graph = collections.defaultdict(set)
		for (u, v) in paths:
			graph[u - 1].add(v - 1)
			graph[v - 1].add(u - 1)

		colors = list(range(1, 4 + 1))
		soln = [-1 for _ in range(N)]
		for u in range(N):
			used = {soln[v] for v in graph[u]}
			for col in colors:
				if col not in used:
					soln[u] = col
					break

		return soln

class Solution(object):
	def gardenNoAdj(self, N, paths):
		graph = collections.defaultdict(set)
		for (u, v) in paths:
			if u > v: 
				graph[u - 1].add(v - 1)
			else:
				graph[v - 1].add(u - 1)

		colors = list(range(1, 4 + 1))
		soln = []
		for u in range(N):
			used = {soln[v] for v in graph[u]}
			for col in colors:
				if col not in used:
					soln.append(col)
					break

		return soln

# After I solve a problem, I like to examine solutions that other people have come up with
# The following is an elegant implementation of the algorithm that I arrived at (though my implementation is faster :-)
# https://leetcode.com/problems/flower-planting-with-no-adjacent/discuss/290858/JavaC%2B%2BPython-Greedily-Paint

class Solution(object):
	def gardenNoAdj(self, N, paths):
		res = [0] * N
		G = [[] for i in range(N)]
		for x, y in paths:
			G[x - 1].append(y - 1)
			G[y - 1].append(x - 1)
		for i in range(N):
			res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
		return res
