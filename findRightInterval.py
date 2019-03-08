# https://leetcode.com/problems/find-right-interval

class Solution:
	def findRightInterval(self, intervals):
		start = sorted(range(len(intervals)), key=lambda i: intervals[i].start)
		finish = sorted(range(len(intervals)), key=lambda i: intervals[i].end)

		i = 0
		j = 0
		right = [-1] * len(intervals)
		while i < len(finish) and j < len(start):
			if intervals[finish[i]].end <= intervals[start[j]].start:
				right[finish[i]] = start[j]
				i += 1
			else:
				j += 1

		return right
