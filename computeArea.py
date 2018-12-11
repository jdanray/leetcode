# https://leetcode.com/problems/rectangle-area/

class Solution:
	def computeArea(self, A, B, C, D, E, F, G, H):
		area1 = (C - A) * (D - B)
		area2 = (G - E) * (H - F)
		total = area1 + area2

		left = max(A, E)
		right = min(C, G)
		bottom = max(B, F)
		top = min(D, H)

		if right > left and top > bottom:
			overlap = (right - left) * (top - bottom)
			total -= overlap

		return total 
