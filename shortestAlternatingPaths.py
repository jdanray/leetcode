# https://leetcode.com/problems/shortest-path-with-alternating-colors/ 

class Solution(object):
	def shortestAlternatingPaths(self, n, red_edges, blue_edges):
		graphRed = collections.defaultdict(set)
		for u, v in red_edges:
			graphRed[u].add(v)

		graphBlue = collections.defaultdict(set)
		for u, v in blue_edges:
			graphBlue[u].add(v)

		seenRed = set()
		seenBlue = set()
		queue = [[0, -1, 0]]
		res = [-1] * n
		while queue:
			vertex, prev, plen = queue.pop(0)

			if res[vertex] == -1:
				res[vertex] = plen

			if prev == 0 or prev == -1:
				for u in graphBlue[vertex]:
					if (u, v) not in seenBlue:
						queue.append([u, 1, plen + 1])
						seenBlue.add((u, v))

			if prev == 1 or prev == -1:
				for u in graphRed[vertex]:
					if (u, v) not in seenRed:
						queue.append([u, 0, plen + 1])
						seenRed.add((u, v))
			
		return res
