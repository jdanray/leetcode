# https://leetcode.com/problems/queens-that-can-attack-the-king/ 

class Solution(object):
	def queensAttacktheKing(self, queens, king):
		N = 8
		hit = set(tuple(q) for q in queens)
		res = []
		for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
			x = king[0]
			y = king[1]
			while x < N and y < N and x >= 0 and y >= 0 and (x, y) not in hit:
				x += dx
				y += dy

			if (x, y) in hit:
				res.append([x, y])

		return res
