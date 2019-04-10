# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
	def sortedSquares(self, A):
		B = [0 for _ in range(len(A))]
		i = 0
		j = len(A) - 1        
		for n in range(len(A))[::-1]:
			if abs(A[i]) > abs(A[j]):
				B[n] = A[i] * A[i]
				i += 1
			else:
				B[n] = A[j] * A[j]
				j -= 1
                
		return B
