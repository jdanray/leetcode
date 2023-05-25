# https://leetcode.com/problems/maximum-performance-of-a-team/ 

class Solution(object):
	def maxPerformance(self, n, speed, efficiency, k):
		MOD = 10**9 + 7

		total = 0
		res = 0
		pq = []
		for (s, e) in sorted(list(zip(speed, efficiency)), key=lambda se: -se[1]):
			heapq.heappush(pq, s)

			total += s
			if len(pq) > k:
				total -= heapq.heappop(pq)

			res = max(res, total * e)

		return res % MOD
