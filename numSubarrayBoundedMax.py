# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

class Solution:
	def numSubarrayBoundedMax(self, A, L, R):
		nsubs = 0
		run = 0
		m = -1
		for i, n in enumerate(A):
			if n < L:
				nsubs += run
			if n > R:
				run = 0
				m = i
			if L <= n and R >= n:
				run = i - m
				nsubs += run
		return nsubs
