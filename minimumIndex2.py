# https://leetcode.com/problems/minimum-capacity-box/

class Solution(object):
	def minimumIndex(self, capacity, itemSize):
		minim = [float('inf'), -1]
		for i, c in enumerate(capacity):
			if c >= itemSize and c < minim[0]:
				minim = [c, i]
		return minim[1]