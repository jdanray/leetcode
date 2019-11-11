# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/

class Solution(object):
	def oddCells(self, n, m, indices):
		matrix = [[0 for _ in range(m)] for _ in range(n)]
		odds = 0
		for ri, ci in indices:
			for j in range(m):
				matrix[ri][j] += 1
				if matrix[ri][j] % 2 == 1:
					odds += 1
				else:
					odds -= 1

			for i in range(n):
				matrix[i][ci]  += 1
				if matrix[i][ci] % 2 == 1:
					odds += 1
				else:
					odds -= 1

		return odds

class Solution(object):
	def oddCells(self, n, m, indices):
		matrix = [[0 for _ in range(m)] for _ in range(n)]
		odds = 0
		for ri, ci in indices:
			for j in range(m):
				matrix[ri][j] += 1
			for i in range(n):
				matrix[i][ci]  += 1

		for i in range(n):
			for j in range(m):
				if matrix[i][j] % 2 == 1:
					odds += 1

		return odds
