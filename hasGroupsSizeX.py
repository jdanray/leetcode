# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/

from collections import Counter

class Solution(object):
	def hasGroupsSizeX(self, deck):
		count = Counter(deck)
		return any(all(count[num] % X == 0 for num in count) for X in range(2, len(deck) + 1))
