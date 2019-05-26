# https://leetcode.com/problems/previous-permutation-with-one-swap/ 

class Solution(object):
	def prevPermOpt1(self, A):
		for i in range(len(A) - 2, -1, -1):
			m = i
			for j in range(i + 1, len(A)):
				if A[j] < A[i] and (m == i or A[j] > A[m]):
					m = j

			if A[m] < A[i]:
				A[i], A[m] = A[m], A[i]
				return A

		return A
