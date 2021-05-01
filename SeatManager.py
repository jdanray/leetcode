# https://leetcode.com/problems/seat-reservation-manager/ 

class SeatManager(object):
	def __init__(self, n):
		self.seats = [i for i in range(1, n + 1)]
	
	def reserve(self):
		return heapq.heappop(self.seats)

	def unreserve(self, seatNumber):
		heapq.heappush(self.seats, seatNumber)
