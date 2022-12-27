# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/ 

class Solution(object):
	def maximumBags(self, capacity, rocks, additionalRocks):
		N = len(capacity)

		pq = [capacity[i] - rocks[i] for i in range(N)]
		heapq.heapify(pq)

		res = 0
		while additionalRocks > 0 and pq:
			c = heapq.heappop(pq)

			r = min(c, additionalRocks)
			c -= r
			additionalRocks -= r 

			if c <= 0:
				res += 1

		return res

class Solution(object):
	def maximumBags(self, capacity, rocks, additionalRocks):
		needed = [capacity[i] - rocks[i] for i in range(len(capacity))]
		needed = sorted(needed)

		res = 0
		for n in needed:
			if additionalRocks >= n:
				additionalRocks -= n
				n = 0

			if n == 0:
				res += 1

		return res
