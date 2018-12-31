# https://leetcode.com/problems/heaters/description/

class Solution:
	def findRadius(self, houses, heaters):
		heaters = sorted(heaters)
		houses = sorted(houses)
		lo = 0
		hi = max(houses[-1], heaters[-1])
		while lo <= hi:
			radius = lo + (hi - lo) // 2
			if self.canHeat(houses, heaters, radius):
				hi = radius - 1
			else:
				lo = radius + 1

		return lo

	def canHeat(self, houses, heaters, radius):
		i = 0
		j = 0
		while i < len(houses) and j < len(heaters):
			if (heaters[j] - radius) <= houses[i] <= (heaters[j] + radius):
				i += 1
			else:
				j += 1

		return i >= len(houses)
