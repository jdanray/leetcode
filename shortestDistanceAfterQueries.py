# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-i/ 

class Solution(object):
	def shortestDistanceAfterQueries(self, n, queries):
		graph = collections.defaultdict(set)
		for u in range(n - 1):
			graph[u].add(u + 1)

		res = []
		for (u, v) in queries:
			graph[u].add(v)

			seen = {0}
			queue = collections.deque([[0, 0]])
			while queue:
				w, d = queue.popleft()

				if w == n - 1:
					res.append(d)
					break

				for x in graph[w]:
					if x not in seen:
						seen.add(x)
						queue.append([x, d + 1])

		return res
