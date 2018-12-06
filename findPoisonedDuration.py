# https://leetcode.com/problems/teemo-attacking/

class Solution(object):
	def findPoisonedDuration(self, timeSeries, duration):
		if not timeSeries:
			return 0

		totaldur = 0
		curstart = timeSeries[0]
		curfinish = curstart + duration
		curdur = curfinish - curstart
		for i in range(1, len(timeSeries)):
			s = timeSeries[i]
			if s >= curfinish:
				totaldur += curdur
				curstart = s
			curfinish = s + duration
			curdur = curfinish - curstart

		return totaldur + curdur

"""
After I solve a problem, I like to see solutions that other people came up with
The following Python solution is too slick not to preserve
"""

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        ans = duration * len(timeSeries)
        for i in range(1,len(timeSeries)):
            ans -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return ans
