# https://leetcode.com/problems/design-ride-sharing-system/

class RideSharingSystem(object):
	def __init__(self):
		self.available = collections.deque([])
		self.waiting = collections.deque([])
		self.riders = set()
		self.cancelled = set()

	def addRider(self, riderId):
		self.riders.add(riderId)
		self.waiting.append(riderId)

	def addDriver(self, driverId):
		self.available.append(driverId)
		
	def matchDriverWithRider(self):
		while self.waiting and self.waiting[0] in self.cancelled:
			self.waiting.popleft()

		if self.waiting and self.available:
			r = self.waiting.popleft()
			d = self.available.popleft()
			return [d, r]
		else:
			return [-1, -1]

	def cancelRider(self, riderId):
		if riderId in self.riders:
			self.cancelled.add(riderId)