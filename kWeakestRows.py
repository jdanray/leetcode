# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/ 

class Solution(object):
	def kWeakestRows(self, mat, k):
		rows = sorted(range(len(mat)), key=lambda i: sum(mat[i]))
		return rows[:k]
