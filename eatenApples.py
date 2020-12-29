# https://leetcode.com/problems/maximum-number-of-eaten-apples/ 

class Solution(object):
	def eatenApples(self, apples, days):
		N = len(days)

		d = 0
		pq = []
		res = 0
		while d < N or pq:
			if d < N and apples[d] != 0:
				heapq.heappush(pq, (d + days[d], apples[d]))

			if not pq:
				d += 1
				continue

			rot, a = heapq.heappop(pq)
			if d < rot:
				res += 1
				d += 1 
				a -= 1
				if a != 0:
					heapq.heappush(pq, (rot, a))

		return res
