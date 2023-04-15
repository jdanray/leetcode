# https://leetcode.com/problems/find-the-width-of-columns-of-a-grid/ 

class Solution(object):
	def findColumnWidth(self, grid):
		return [max(len(str(grid[i][j])) for i in range(len(grid))) for j in range(len(grid[0]))]

class Solution(object):
	def findColumnWidth(self, grid):
		M = len(grid)
		N = len(grid[0])

		res = []
		for j in range(N):
			width = max(len(str(grid[i][j])) for i in range(M))
			res.append(width)	

		return res

class Solution(object):
	def findColumnWidth(self, grid):
		M = len(grid)
		N = len(grid[0])

		res = []
		for j in range(N):
			width = 0
			for i in range(M):
				l = 0
				n = grid[i][j]
				if n < 0:
					n = abs(n)
					l += 1

				if n == 0:
					l = 1

				while n > 0:
					l += 1
					n //= 10

				width = max(width, l)

			res.append(width)	

		return res	
