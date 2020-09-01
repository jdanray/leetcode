# https://leetcode.com/problems/last-stone-weight/

class Solution:
	def lastStoneWeight(self, stones):
		if not stones:
			return 0

		stones = sorted(stones)
		y = stones.pop()
		if not stones:
			return y

		x = stones.pop()
		if x == y:
			return self.lastStoneWeight(stones)

		return self.lastStoneWeight(stones + [y - x])

class Solution(object):
	def lastStoneWeight(self, stones):
		stones = [-s for s in stones]
		heapq.heapify(stones)
		while len(stones) >= 2:
			x = heapq.heappop(stones)
			y = heapq.heappop(stones)

			if x != y:
				heapq.heappush(stones, x - y)

		return abs(stones[0]) if stones else 0
