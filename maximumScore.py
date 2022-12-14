# https://leetcode.com/problems/maximum-score-from-removing-stones/

class Solution(object):
	def maximumScore(self, a, b, c):
		pq = [a, b, c]
		heapq.heapify(pq)

		res = 0
		while pq:
			# x <= y <= z
			x = heapq.heappop(pq)
			y = heapq.heappop(pq)
			z = heapq.heappop(pq)

			if y == 0:
				return res
			elif x == 0:
				return res + y

			d = (y - x) + 1
			y -= d
			z -= d
			res += d

			heapq.heappush(pq, x)
			heapq.heappush(pq, y)
			heapq.heappush(pq, z)

		return res
