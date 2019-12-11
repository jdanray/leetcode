# https://leetcode.com/problems/number-of-recent-calls/ 

class RecentCounter(object):
	def __init__(self):
		self.N = 3000
		self.pings = []

	def ping(self, t):
		self.pings.append(t)
		start = bisect.bisect_left(self.pings, t - self.N)
		return len(self.pings) - start
