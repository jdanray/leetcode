# https://leetcode.com/problems/fair-candy-swap/description/

class Solution:
	def fairCandySwap(self, A, B):
		dBA = sum(B) - sum(A)
		alice = {}
		for a in A:
			alice[dBA + 2 * a] = a
		for b in B:
			twiceb = 2 * b
			if twiceb in alice:
				return [alice[twiceb], b]
