3 https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

class Solution(object):
	def kthSmallest(self, matrix, k):
		N = len(matrix)
		pq = []
		for i in range(N):
			heapq.heappush(pq, (matrix[i][0], i, 0))

		for _ in range(k - 1):
			n, i, j = heapq.heappop(pq)

			if j + 1 < N:
				heapq.heappush(pq, (matrix[i][j + 1], i, j + 1))

		return pq[0][0]
