# https://leetcode.com/problems/rotate-string/

class Solution(object):
	def rotateString(self, A, B):
		if A == B:
			return True

		for _ in range(len(A)):
			A = A[1:] + A[0]
			if A == B:
				return True

		return False
