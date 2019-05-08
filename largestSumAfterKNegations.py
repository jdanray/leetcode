# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

class Solution(object):
	def largestSumAfterKNegations(self, A, K):
		pq = [(n, i) for i, n in enumerate(A)]
		heapq.heapify(pq)
		for _ in range(K):
			(_, m) = heapq.heappop(pq)
			A[m] = -A[m]
			heapq.heappush(pq, (A[m], m))

		return sum(A)

class Solution(object):
	def largestSumAfterKNegations(self, A, K):
		for _ in range(K):
			m = min(range(len(A)), key=lambda i: A[i])
			A[m] = -A[m]

		return sum(A)
