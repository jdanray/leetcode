# https://leetcode.com/problems/arithmetic-slices

class Solution:
	def numberOfArithmeticSlices(self, A):
		if len(A) < 3:
			return 0

		p = 0
		nslices = 0
		for i in range(2, len(A)):
			if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
				p += 1
				nslices += p
			else:
				p = 0

		return nslices
