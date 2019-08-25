# https://leetcode.com/problems/minimum-time-difference/ 

class Solution(object):
	def findMinDifference(self, timePoints):
		times = []
		for t in timePoints:
			hours, mins = map(int, t.split(':'))
			times.append(60 * hours + mins)

		MOD = 24 * 60
		times = sorted(times)
		res = MOD
		for i in range(len(times)):
			res = min(res, (times[i] - times[i - 1]) % MOD)
		return res
