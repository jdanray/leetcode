# https://leetcode.com/problems/n-queens/

class Solution(object):
	def solveNQueens(self, n, sol=[]):
		nrows = len(sol)
		if nrows == n:
			return [sol]

		solutions = []
		for col in range(n):
			if any(row[col] == 'Q' for row in sol): continue

			if any(col + (nrows - r) < n and sol[r][col + (nrows - r)] == 'Q' for r in range(nrows)): continue
			if any(col - (nrows - r) >= 0 and sol[r][col - (nrows - r)] == 'Q' for r in range(nrows)): continue

			new_row = [('.' * col) + 'Q' + ('.' * (n - col - 1))]
			solutions += self.solveNQueens(n, sol + new_row)

		return solutions
