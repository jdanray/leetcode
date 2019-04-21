# https://leetcode.com/problems/matrix-cells-in-distance-order/

class Solution:
	def allCellsDistOrder(self, R, C, r0, c0):
		allcoords = [(r, c) for r in range(R) for c in range(C)]
		return list(sorted(allcoords, key=lambda coord: abs(coord[0] - r0) + abs(coord[1] - c0)))
