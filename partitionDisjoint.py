# https://leetcode.com/problems/partition-array-into-disjoint-intervals/

class Solution(object):
	def partitionDisjoint(self, A):
		m = A[0]
		t = A[0]
		l = 0
		for i in range(1, len(A)):
			if A[i] > m:
				m = A[i]
			if A[i] < t:
				l = i
				t = m
		return l + 1

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
