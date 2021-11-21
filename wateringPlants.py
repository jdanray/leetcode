# https://leetcode.com/problems/watering-plants/

class Solution(object):
	def wateringPlants(self, plants, capacity):
		can = capacity
		res = 0
		for i, p in enumerate(plants):
			if p > can:
				res += i
				can = capacity
				res += i
	
			res += 1
			can -= p

		return res
