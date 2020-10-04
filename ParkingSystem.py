# https://leetcode.com/problems/design-parking-system/ 

class ParkingSystem(object):
	def __init__(self, big, medium, small):
		self.slots = [big, medium, small]

	def addCar(self, carType):
		if self.slots[carType - 1] == 0:
			return False
		else:
			self.slots[carType - 1] -= 1
			return True
