# https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream(object):
	def __init__(self, value, k):
		self.value = value
		self.k = k
		self.last = 0

	def consec(self, num):
		if num == self.value:
			self.last += 1
		else:
			self.last = 0

		return self.last >= self.k
