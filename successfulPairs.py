# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/

class Solution(object):
	def successfulPairs(self, spells, potions, success):
		potions = sorted(float(success) / p for p in potions)
		return [bisect.bisect(potions, s) for s in spells]
