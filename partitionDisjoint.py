# https://leetcode.com/problems/partition-array-into-disjoint-intervals/

class Solution:
	def partitionDisjoint(self, A):
		left = 1
		m = 0
		for i in range(1, len(A)):
			if A[i] > A[m]:
				m = i
			if A[i] < A[0] or (m < left and A[i] < A[m]):
				left = i + 1
		return left
