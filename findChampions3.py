# https://leetcode.com/problems/find-champion-ii/

class Solution(object):
	def findChampion(self, n, edges):
		weak = {v for (_, v) in edges}
		cands = {u for u in range(n) if u not in weak}
		return next(iter(cands)) if len(cands) == 1 else -1