# https://leetcode.com/problems/toggle-light-bulbs/

class Solution(object):
	def toggleLightBulbs(self, bulbs):
		on = collections.defaultdict(bool)
		for b in bulbs:
			on[b] = not on[b]

		return sorted([b for b in on if on[b]])