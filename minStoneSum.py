# https://leetcode.com/problems/remove-stones-to-minimize-the-total/ 

class Solution(object):
	def minStoneSum(self, piles, k):
		piles = [-p for p in piles]
		heapq.heapify(piles)
		for _ in range(k):
			top = heapq.heappop(piles)
			top = floor(top / 2)
			heapq.heappush(piles, top)

		return int(abs(sum(piles)))
