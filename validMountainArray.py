# https://leetcode.com/contest/weekly-contest-111/problems/valid-mountain-array/

class Solution:
	def validMountainArray(self, A):
		if len(A) < 3:
			return False

		ascending = False
		descending = False
		for i in range(len(A) - 1):
			if A[i] == A[i + 1]:
				return False

			if A[i] < A[i + 1]:
				if not ascending:
					if descending:
						return False
					ascending = True

			if A[i] > A[i + 1]:
				if not descending and ascending:
					descending = True
					ascending = False
				elif not descending and not ascending:
					return False

		return descending and not ascending
