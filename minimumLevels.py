# https://leetcode.com/problems/minimum-levels-to-gain-more-points/ 

class Solution(object):
	def minimumLevels(self, pos):
		b = 0
		for p in pos:
			if p == 1:
				b += 1
			else:
				b -= 1

		d = 0
		for i in range(len(pos) - 1):
			if pos[i] == 1:
				d += 1
				b -= 1
			else:
				d -= 1
				b += 1

			if d > b:
				return i + 1

		return -1
