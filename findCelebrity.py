# https://leetcode.com/problems/find-the-celebrity/

class Solution(object):
	def findCelebrity(n):
		A = 0
		for B in range(1, n):
			if knows(A, B):
				A = B

		for B in range(n):
			if B == A:
				continue

			if not knows(B, A) or knows(A, B):
				return -1

		return A
