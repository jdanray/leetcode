# https://leetcode.com/problems/largest-plus-sign/ 

class Solution(object):
	def orderOfLargestPlusSign(self, n, mines):
		mines = set(tuple([x, y]) for (x, y) in mines)

		left = [[0 for _ in range(n)] for _ in range(n)]
		right = [[0 for _ in range(n)] for _ in range(n)]
		for i in range(n):
			for j in range(n):
				if (i, j) not in mines:
					if j - 1 >= 0:
						left[i][j] = left[i][j - 1] + 1
					else:
						left[i][j] = 1

			for j in range(n - 1, -1, -1):
				if (i, j) not in mines:
					if j + 1 < n:
						right[i][j] = right[i][j + 1] + 1
					else:
						right[i][j] = 1

		up = [[0 for _ in range(n)] for _ in range(n)]
		down = [[0 for _ in range(n)] for _ in range(n)]
		for j in range(n):
			for i in range(n):
				if (i, j) not in mines:
					if i - 1 >= 0:
						up[i][j] = up[i - 1][j] + 1
					else:
						up[i][j] = 1

			for i in range(n - 1, -1, -1):
				if (i, j) not in mines:
					if i + 1 < n:
						down[i][j] = down[i + 1][j] + 1
					else:
						down[i][j] = 1

		res = 0
		for i in range(n):
			for j in range(n):
				if (i, j) not in mines:
					res = max(res, min(left[i][j], right[i][j], down[i][j], up[i][j]))

		return res
