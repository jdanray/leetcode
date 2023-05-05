# https://leetcode.com/problems/count-sub-islands/

class Solution(object):
	def countSubIslands(self, grid1, grid2):
		M = len(grid1)
		N = len(grid1[0])

		def dfs(i, j):
			if i < 0 or i >= M or j < 0 or j >= N or grid2[i][j] == 0:
				return True

			grid2[i][j] = 0
            
			a = dfs(i + 1, j)
			b = dfs(i - 1, j)
			c = dfs(i, j + 1)
			d = dfs(i, j - 1)

			return grid1[i][j] == 1 and a and b and c and d

		return sum(grid2[i][j] == 1 and dfs(i, j) for i in range(M) for j in range(N))
