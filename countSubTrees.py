# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/ 

class Solution(object):
	def countSubTrees(self, n, edges, labels):
		N = 26
		alpha = 'abcdefghijklmnopqrstuvwxyz'
		alphanum = {c: i for i, c in enumerate(alpha)}

		graph = collections.defaultdict(set)
		for u, v in edges:
			graph[u].add(v)
			graph[v].add(u)

		res = [0 for _ in range(n)]
		visited = set()
		def dfs(u):
			count = [0 for _ in range(N)]
			if u in visited:
				return count

			visited.add(u)
			for v in graph[u]:
				s = dfs(v)
				for l in range(N):
					count[l] += s[l]

			c = alphanum[labels[u]]
			count[c] += 1
			res[u] = count[c]
			return count

		dfs(0)
		return res
