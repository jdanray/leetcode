# https://leetcode.com/problems/ipo/

class Solution(object):
	def findMaximizedCapital(self, k, W, Profits, Capital):
		pqpro = []
		pqcap = zip(Capital, Profits)
		heapq.heapify(pqcap)

		for _ in range(k):
			while pqcap and pqcap[0][0] <= W:
				_, p = heapq.heappop(pqcap)
				heapq.heappush(pqpro, -p)

			if not pqpro:
				break
			
			W -= heapq.heappop(pqpro) 

		return W 
