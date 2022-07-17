# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/ 

class Solution(object):
	def fillCups(self, amount):
		pq = [-a for a in amount if a > 0]
		heapq.heapify(pq)
		res = 0
		while pq:
			a = heapq.heappop(pq)
			if pq:
				b = heapq.heappop(pq)
				res += 1
				if b + 1 < 0:
					heapq.heappush(pq, b + 1)
			else:
				res += 1

			if a + 1 < 0:
				heapq.heappush(pq, a + 1)

		return res
