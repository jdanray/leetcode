# https://leetcode.com/problems/insert-interval/

# Repurposing my code for merging overlapping intervals
# Simply add newInterval to the list of intervals, and merge all intervals
class Solution(object):
	def insert(self, intervals, newInterval):
		intervals.append(newInterval)

		intervals = sorted(intervals, key=lambda i: i[0])
		res = [intervals[0]]
		for i in range(1, len(intervals)):
			if intervals[i][0] <= res[-1][1]:
				res[-1][1] = max(res[-1][1], intervals[i][1])
			else:
				res.append(intervals[i])

		return res
