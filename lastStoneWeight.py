# https://leetcode.com/problems/last-stone-weight/

class Solution(object):
	def lastStoneWeight(self, stones):
		pq = [-s for s in stones]
		heapq.heapify(pq)

		while len(pq) > 1:
			u = heapq.heappop(pq)
			v = heapq.heappop(pq)

			if u != v:
				heapq.heappush(pq, u - v)

		return abs(pq[0]) if pq else 0
