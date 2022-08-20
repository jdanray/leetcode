# https://leetcode.com/problems/node-with-highest-edge-score/

class Solution(object):
	def edgeScore(self, edges):
		score = collections.defaultdict(int)
		maxScore = 0
		for (u, v) in enumerate(edges):
			score[v] += u
			maxScore = max(maxScore, score[v])

		for v in range(len(edges)):
			if score[v] == maxScore:
				return v
