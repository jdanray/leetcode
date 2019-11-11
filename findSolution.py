# https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/

class Solution(object):
	def findSolution(self, customfunction, z):
		seen = set()
		res = []
		def g(x, y):
			if (x, y) not in seen:
				seen.add((x, y))
				v = customfunction.f(x, y)
				if v == z:
					res.append([x, y])
				elif v < z:
					g(x + 1, y)
					g(x, y + 1)

		g(1, 1)
		return res
