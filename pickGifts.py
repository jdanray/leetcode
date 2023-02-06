# https://leetcode.com/problems/take-gifts-from-the-richest-pile/ 

class Solution(object):
	def pickGifts(self, gifts, k):
		gifts = [-g for g in gifts]
		heapq.heapify(gifts)

		res = 0
		for _ in range(k):
			g = heapq.heappop(gifts)
			g = -g
			sq = math.floor(math.sqrt(g))
			heapq.heappush(gifts, -sq)

		return -int(sum(gifts))
