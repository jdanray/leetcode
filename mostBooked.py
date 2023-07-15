# https://leetcode.com/problems/meeting-rooms-iii/ 

class Solution(object):
	def mostBooked(self, n, meetings):
		meetings = [[s, f - s] for (s, f) in meetings]
		meetings = sorted(meetings)

		availRooms = list(range(n))
		usedRooms = []

		count = collections.Counter()
		curTime = 0
		res = -1
		maxc = 0
		for (start, dur) in meetings:
			curTime = max(curTime, start)

			while usedRooms and usedRooms[0][0] <= curTime:
				_, r = heapq.heappop(usedRooms)
				heapq.heappush(availRooms, r)

			if not availRooms:
				f, r = heapq.heappop(usedRooms)
				heapq.heappush(availRooms, r)
				curTime = f

			r = heapq.heappop(availRooms)
			count[r] += 1
			heapq.heappush(usedRooms, (curTime + dur, r))

			if count[r] > maxc or (count[r] == maxc and r < res):
				res = r
				maxc = count[r]

		return res
