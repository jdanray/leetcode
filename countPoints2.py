# https://leetcode.com/problems/rings-and-rods/

class Solution(object):
	def countPoints(self, rings):
		NCOLORS = 3

		rods = collections.defaultdict(set)
		for i in range(0, len(rings), 2):
			rods[rings[i + 1]].add(rings[i])

		return len([r for r in rods if len(rods[r]) == NCOLORS])
