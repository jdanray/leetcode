# https://leetcode.com/problems/groups-of-special-equivalent-strings/ 

class Solution(object):
	def numSpecialEquivGroups(self, words):
		groups = set()
		for w in words:
			even = sorted(w[i] for i in range(0, len(w), 2))
			odd = sorted(w[i] for i in range(1, len(w), 2))
			s = ''.join(even + odd)
			groups.add(s)

		return len(groups)
