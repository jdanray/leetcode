# https://leetcode.com/problems/shortest-path-with-alternating-colors/ 

class Solution(object):
	def shortestAlternatingPaths(self, n, red_edges, blue_edges):
		ans = [-1 for _ in range(n)]
		
		reds = collections.defaultdict(set)
		for u, v in red_edges:
			reds[u].add(v)

		blues = collections.defaultdict(set)
		for u, v in blue_edges:
			blues[u].add(v)

		usedred = set()
		usedblue = set()
		queue = [[0, -1, 0]]
		while queue:
			vertex, prev, path = queue.pop(0)

			if ans[vertex] == -1 or path < ans[vertex]:
				ans[vertex] = path

			if prev == -1:
				for u in blues[vertex]:
					if (u, v) not in usedblue:
						queue.append([u, 1, path + 1])
						usedblue.add((u, v))
				for u in reds[vertex]:
					if (u, v) not in usedred:
						queue.append([u, 0, path + 1])				
						usedred.add((u, v))

			if prev == 0:
				for u in blues[vertex]:
					if (u, v) not in usedblue:
						queue.append([u, 1, path + 1])
						usedblue.add((u, v))

			if prev == 1:
				for u in reds[vertex]:
					if (u, v) not in usedred:
						queue.append([u, 0, path + 1])
						usedred.add((u, v))
			
		return ans
