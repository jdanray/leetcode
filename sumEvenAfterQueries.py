# https://leetcode.com/problems/sum-of-even-numbers-after-queries/

class Solution(object):
	def sumEvenAfterQueries(self, A, queries):
		s = sum(a for a in A if a % 2 == 0)
		sums = []
		for val, idx in queries:
			if A[idx] % 2 == 0:
				s -= A[idx]

			A[idx] += val
			if A[idx] % 2 == 0:
				s += A[idx]

			sums.append(s)
		return sums
