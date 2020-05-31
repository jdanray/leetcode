# https://leetcode.com/problems/number-of-boomerangs/

class Solution(object):
	def numberOfBoomerangs(self, points):
		def dist(x1, y1, x2, y2):
			return (x2 - x1) ** 2 + (y2 - y1) ** 2

		res = 0
		for i, p1 in enumerate(points):
			distances = collections.defaultdict(int)
			for j, p2 in enumerate(points):
				if i == j:
					continue

				d = dist(p1[0], p1[1], p2[0], p2[1])
				distances[d] += 1

			for d in distances:
				res += distances[d] * (distances[d] - 1)

		return res
