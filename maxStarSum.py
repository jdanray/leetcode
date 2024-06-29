# https://leetcode.com/problems/maximum-star-sum-of-a-graph/ 

from sortedcontainers import SortedList

class Solution(object):
	def maxStarSum(self, vals, edges, k):
		starVals = collections.defaultdict(SortedList)
		starSum = {i: v for i, v in enumerate(vals)}

		res = max(vals)
		for (u, v) in edges:
			for (x, y) in [[u, v], [v, u]]:
				if vals[y] < 0:
					continue

				if len(starVals[x]) == k and starVals[x] and vals[y] > starVals[x][0]:
					starSum[x] -= starVals[x].pop(0)

				if len(starVals[x]) < k:
					starSum[x] += vals[y]
					starVals[x].add(vals[y])

				res = max(res, starSum[x])

		return res
