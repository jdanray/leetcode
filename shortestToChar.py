# https://leetcode.com/problems/shortest-distance-to-a-character/description/

class Solution:
	def shortestToChar(self, S, C):
		pt = [i for i, c in enumerate(S) if c == C]
		dists = []
		j = 0
		for i, c in enumerate(S):
			d1 = abs(i - pt[j])
			if j + 1 >= len(pt):
				dists.append(d1)
			else:
				d2 = abs(i - pt[j + 1])
				if d1 >= d2:
					j += 1
				dists.append(min(d1, d2))
		return dists
