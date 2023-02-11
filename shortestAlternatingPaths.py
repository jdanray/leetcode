# https://leetcode.com/problems/shortest-path-with-alternating-colors/ 

class Solution(object):
	def shortestAlternatingPaths(self, n, redEdges, blueEdges):
		graphRed = collections.defaultdict(set)
		for (u, v) in redEdges:
			graphRed[u].add(v)

		graphBlue = collections.defaultdict(set)
		for (u, v) in blueEdges:
			graphBlue[u].add(v)

		seenRed = set()
		seenBlue = set()
		queue = collections.deque([[0, -1, 0]])
		res = [-1] * n
		while queue:
			u, prev, plen = queue.popleft()

			if res[u] == -1:
				res[u] = plen

			if prev == 0 or prev == -1:
				for v in graphBlue[u]:
					if (u, v) not in seenBlue:
						queue.append([v, 1, plen + 1])
						seenBlue.add((u, v))

			if prev == 1 or prev == -1:
				for v in graphRed[u]:
					if (u, v) not in seenRed:
						queue.append([v, 0, plen + 1])
						seenRed.add((u, v))
			
		return res
