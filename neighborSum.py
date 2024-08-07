# https://leetcode.com/problems/design-neighbor-sum-service/ 

class neighborSum(object):
	def __init__(self, grid):
		self.adj = collections.defaultdict(int)
		self.diag = collections.defaultdict(int)
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if i - 1 >= 0:
					self.adj[grid[i][j]] += grid[i - 1][j]
                    
					if j - 1 >= 0:
						self.diag[grid[i][j]] += grid[i - 1][j - 1]
					if j + 1 < len(grid):
						self.diag[grid[i][j]] += grid[i - 1][j + 1]

				if i + 1 < len(grid):
					self.adj[grid[i][j]] += grid[i + 1][j]
                    
					if j - 1 >= 0:
						self.diag[grid[i][j]] += grid[i + 1][j - 1]
					if j + 1 < len(grid):
						self.diag[grid[i][j]] += grid[i + 1][j + 1]

				if j - 1 >= 0:
					self.adj[grid[i][j]] += grid[i][j - 1]

				if j + 1 < len(grid):
					self.adj[grid[i][j]] += grid[i][j + 1]

	def adjacentSum(self, value):
		return self.adj[value]

	def diagonalSum(self, value):
		return self.diag[value]
