# https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution(object):
	def addToArrayForm(self, A, K):
		i = len(A) - 1
		while i >= 0 and K > 0:
			A[i] += K
			K = A[i] // 10
			if A[i] >= 10:
				A[i] %= 10
				if i == 0:
					A = [0] + A
					i += 1
			i -= 1
		return A
