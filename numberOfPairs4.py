# https://leetcode.com/problems/find-the-number-of-ways-to-place-people-i/

class Solution(object):
	def numberOfPairs(self, points):
		N = len(points)

		points = sorted(points, key=lambda p: (-p[1], p[0]))

		res = 0
		for i in range(N):
			x1, y1 = points[i]
            
			for j in range(i):
				x2, y2 = points[j]

				if x1 < x2:
					continue

				good = True
				for k in range(N):
					if k == i or k == j:
						continue

					x3, y3 = points[k]

					if x2 <= x3 <= x1 and y2 >= y3 >= y1:
						good = False
						break

				if good:
					res += 1

		return res