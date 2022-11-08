# https://leetcode.com/problems/total-cost-to-hire-k-workers/ 

class Solution(object):
	def totalCost(self, costs, k, cands):
		N = len(costs)

		mid = collections.deque()
		l = cands
		r = N - cands - 1

		pq = []
		heapq.heapify(pq)

		for i, c in enumerate(costs):
			if i < cands or i >= N - cands:
				heapq.heappush(pq, (c, i))
			else:
				mid.append(c)

		res = 0
		for _ in range(k):
			c, i = heapq.heappop(pq)

			res += c

			if not mid:
				continue

			if i < l:
				m = mid.popleft()
				heapq.heappush(pq, (m, l))
				l += 1
			else:
				m = mid.pop()
				heapq.heappush(pq, (m, r))
				r -= 1

		return res
