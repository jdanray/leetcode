# https://leetcode.com/problems/ipo/

class Solution(object):
	def findMaximizedCapital(self, k, w, profits, capital):
		maxProf = []
		minCap = zip(capital, profits)
		heapq.heapify(minCap)

		for _ in range(k):
			while minCap and minCap[0][0] <= w:
				_, p = heapq.heappop(minCap)
				heapq.heappush(maxProf, -p)

			if not maxProf:
				break
			
			w -= heapq.heappop(maxProf) 

		return w 
