# https://leetcode.com/problems/count-nodes-with-the-highest-score/ 

class Solution(object):
	def countHighestScoreNodes(self, parents):
		N = len(parents)

		children = [[] for _ in range(N)]
		root = -1
		for u in range(N):
			if parents[u] != -1:
				children[parents[u]].append(u)
			else:
				root = u

		size = [1 for _ in range(N)]
		def calcSize(u):
			for v in children[u]:
				size[u] += calcSize(v)
			return size[u]

		calcSize(root)

		maxScore = 0
		res = 0
		for u in range(N):
			if u == root:
				score = 1
			else:
				score = size[root] - size[u]

			for v in children[u]:
				score *= size[v]

			if score > maxScore:
				maxScore = score
				res = 1
			elif score == maxScore:
				res += 1

		return res
