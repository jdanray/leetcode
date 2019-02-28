# https://leetcode.com/problems/find-the-town-judge/

class Solution(object):
	def findJudge(self, N, trust):
		nin = {u: 0 for u in range(1, N + 1)}
		outs = set()

		for u, v in trust:
			nin[v] += 1
			outs.add(u)

		for u in range(1, N + 1):
			if nin[u] == N - 1 and u not in outs:
				return u

		return -1
