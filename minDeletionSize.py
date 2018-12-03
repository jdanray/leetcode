# https://leetcode.com/contest/weekly-contest-111/problems/delete-columns-to-make-sorted/

class Solution(object):
	def minDeletionSize(self, A):
		return sum(1 if any(A[i][c] > A[i + 1][c] for i in range(len(A) - 1)) else 0 for c in range(len(A[0])))
