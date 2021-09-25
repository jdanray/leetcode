# https://leetcode.com/problems/cinema-seat-allocation/

class Solution(object):
	def maxNumberOfFamilies(self, n, reservedSeats):
		N = len(reservedSeats)
		fourSeats = [[2,3,4,5],[4,5,6,7],[6,7,8,9]]

		reservedSeats = sorted(reservedSeats)

		i = 0
		res = 0
		rowSeen = 0
		while i < N:
			row = reservedSeats[i][0]
			rowSeen += 1

			reserved = set()
			while i < N and reservedSeats[i][0] == row:
				seat = reservedSeats[i][1]
				reserved.add(seat)
				i += 1

			for seats in fourSeats:
				if all(s not in reserved for s in seats):
					res += 1
					for s in seats:
						reserved.add(s)

		return res + 2 * (n - rowSeen)
