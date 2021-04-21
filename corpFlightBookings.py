# https://leetcode.com/problems/corporate-flight-bookings/ 

class Solution(object):
	def corpFlightBookings(self, bookings, n):
		delta = [0 for _ in range(n)]
		for (first, last, seats) in bookings:
			delta[first - 1] += seats
			if last < n:
				delta[last] -= seats

		res = [0 for _ in range(n)]
		tot = 0
		for i in range(n):
			tot += delta[i]
			res[i] = tot
		return res
