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
