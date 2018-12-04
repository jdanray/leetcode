# https://leetcode.com/contest/weekly-contest-112/problems/minimum-increment-to-make-array-unique/ 

class Solution(object):
	def minIncrementForUnique(self, A):
		A = sorted(A)
		nmoves = 0
		for i in range(1, len(A)):
			if A[i] <= A[i - 1]:
				nmoves += A[i - 1] + 1 - A[i]
				A[i] = A[i - 1] + 1
		return nmoves

