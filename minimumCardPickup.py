# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/ 

class Solution(object):
	def minimumCardPickup(self, cards):
		seen = {}
		res = float('inf')
		for i, c in enumerate(cards):
			if c in seen:
				res = min(res, i - seen[c])

			seen[c] = i

		return -1 if res == float('inf') else res + 1
