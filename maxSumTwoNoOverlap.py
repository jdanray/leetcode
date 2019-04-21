# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

class Solution:
	def maxSumTwoNoOverlap(self, A, L, M):
		maxi = 0
		for i in range(len(A) - L + 1):
			s1 = sum(A[i:i + L])
			for j in range(i - M + 1):
				s2 = sum(A[j:j + M])
				maxi = max(maxi, s1 + s2)

			for j in range(i + L, len(A) - M + 1):
				s2 = sum(A[j:j + M])
				maxi = max(maxi, s1 + s2)

		return maxi
