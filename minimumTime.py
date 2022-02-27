# https://leetcode.com/problems/minimum-time-to-complete-trips/

class Solution(object):
	def minimumTime(self, time, totalTrips):
		def condition(value):
			return sum(value // t for t in time) >= totalTrips

		left = 1
		right = time[-1] * totalTrips
		while left < right:
			mid = left + (right - left) // 2

			if condition(mid):
				right = mid
			else:
				left = mid + 1

		return left
