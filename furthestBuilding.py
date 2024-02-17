# https://leetcode.com/problems/furthest-building-you-can-reach/ 

class Solution(object):
	def furthestBuilding(self, h, b, l):
		pq = []
		for i in range(len(h) - 1):
			d = h[i + 1] - h[i]
			if d <= 0:
				continue

			heapq.heappush(pq, -d)
			b -= d

			if b < 0:
				if l == 0:
					return i
				else:
					l -= 1
					b -= heapq.heappop(pq)

		return len(h) - 1
