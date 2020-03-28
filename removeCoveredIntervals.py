# https://leetcode.com/problems/remove-covered-intervals 

class Solution(object):
	def removeCoveredIntervals(self, intervals):
		intervals = sorted(intervals)
		maxb = 0
		rem = 0
		for a, b in intervals:
			if b <= maxb:
				res += 1
			maxb = max(maxb, b)

		return len(intervals) - rem
