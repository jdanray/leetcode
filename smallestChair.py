# https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

class Solution(object):
	def smallestChair(self, times, targetFriend):
		party = sorted((a, l, f) for f, (a, l) in enumerate(times))

		available = []
		occupied = []
		heapq.heapify(available)
		heapq.heapify(occupied)

		freed = 0
        
		for t, (arrival, leaving, friend) in enumerate(party):
			while occupied and occupied[0][0] <= arrival:
				_, s = heapq.heappop(occupied)
				heapq.heappush(available, s)

			if available:
				seat = heapq.heappop(available)
				freed += 1
			else:
				seat = t - freed

			if friend == targetFriend:
				return seat
			else:
				heapq.heappush(occupied, (leaving, seat))