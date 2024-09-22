# https://leetcode.com/problems/k-th-nearest-obstacle-queries/submissions/ 

from sortedcontainers import SortedList

class Solution(object):
	def resultsArray(self, queries, k):
		sl = SortedList()
		res = []
		for (x, y) in queries:
			dist = abs(x) + abs(y)
			sl.add(dist)

			if len(sl) >= k:
				res.append(sl[k - 1])
			else:
				res.append(-1)

		return res
