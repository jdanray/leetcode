# https://leetcode.com/problems/non-overlapping-intervals/

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
	def eraseOverlapIntervals(self, intervals):
		if not intervals:
			return 0

		n = 1
		o = 0
		intervals = sorted(intervals, key=lambda i: i.end)
		for i in range(1, len(intervals)):
			if intervals[i].start >= intervals[o].end:
				o = i
				n += 1

		return len(intervals) - n
