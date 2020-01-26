# https://leetcode.com/problems/rank-transform-of-an-array/ 

class Solution(object):
	def arrayRankTransform(self, arr):
		rank = {n: i + 1 for i, n in enumerate(sorted(set(arr)))}
		return [rank[n] for n in arr]
