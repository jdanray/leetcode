# https://leetcode.com/problems/baseball-game/description/

class Solution:
	def calPoints(self, ops):
		pts = []
		for o in ops:
			if o == '+':
				pts.append(pts[-1] + pts[-2])
			elif o == 'D':
				pts.append(pts[-1] + pts[-1])
			elif o == 'C':
				pts = pts[:-1]
			else:
				pts.append(int(o))
		return sum(pts)
