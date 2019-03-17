# https://leetcode.com/problems/merge-intervals/

class Solution:
	def merge(self, intervals):
		if not intervals:
			return []

		intervals = sorted(intervals, key=lambda i: i.start)

		res = [intervals[0]]
		for i in range(1, len(intervals)):
			if intervals[i].start <= res[-1].end:
				res[-1].end = max(res[-1].end, intervals[i].end)
			else:
				res.append(intervals[i])

		return res
