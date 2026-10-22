# https://leetcode.com/problems/minimize-the-maximum-waiting-time-at-synchronized-traffic-lights/ 

class Solution(object):
	def minPenalty(self, period, lights, arrivalTime):
		m = max(lights)
		res = 0
		for a in arrivalTime:
			r = a % period
			if r >= m:
				res = max(res, period - r)
		return res
