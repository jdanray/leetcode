# https://leetcode.com/problems/n-queens-ii/

class Solution(object):
	def totalNQueens(self, n, sol=[]):
		col = len(sol)
		if col == n:
			return 1

		solutions = 0
		for row in range(n):
			if row in sol: continue

			sol_cols = range(col)
			if row + col in [sol[c] + c for c in sol_cols]: continue
			if row - col in [sol[c] - c for c in sol_cols]: continue

			solutions += self.totalNQueens(n, sol + [row]) 

		return solutions
