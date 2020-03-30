# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem(object):
	def __init__(self):
		self.checkin = {}
		self.travelTime = collections.defaultdict(list)

	def checkIn(self, id, stationName, t):
		self.checkin[id] = (stationName, t)

	def checkOut(self, id, stationName, t):
		startStation, startTime = self.checkin[id]
		self.travelTime[startStation, stationName].append(float(t - startTime))

	def getAverageTime(self, startStation, endStation):
		return sum(self.travelTime[startStation, endStation]) / len(self.travelTime[startStation, endStation])
