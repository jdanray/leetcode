# https://leetcode.com/problems/distance-between-bus-stops/ 

class Solution(object):
	def distanceBetweenBusStops(self, distance, start, destination):
		forward = 0
		loc = start
		while loc != destination:
			forward += distance[loc]
			loc += 1
			loc %= len(distance)

		backward = 0
		loc = start
		while loc != destination:
			loc -= 1
			loc %= len(distance)
			backward += distance[loc]

		return min(forward, backward)
