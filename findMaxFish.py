# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/ 

class Solution(object):
	def findMaxFish(self, grid):
		M = len(grid)
		N = len(grid[0])

		def dfs(i, j):
			if i < 0 or i >= M or j < 0 or j >= N or grid[i][j] == 0:
				return 0

			res = grid[i][j]

			grid[i][j] = 0
            
			res += dfs(i + 1, j)
			res += dfs(i - 1, j)
			res += dfs(i, j + 1)
			res += dfs(i, j - 1)

			return res

		return max(dfs(i, j) for i in range(M) for j in range(N))

class Solution(object):
	def findMaxFish(self, grid):
		M = len(grid)
		N = len(grid[0])

		def dfs(i, j):
			deltas = [[1, 0], [-1, 0], [0, 1], [0, -1]]

			res = 0
			seen = {(i, j)}
			stack = [(i, j)]
			while stack:
				k, l = stack.pop()

				if k < 0 or k >= M or l < 0 or l >= N or grid[k][l] == 0:
					continue

				res += grid[k][l]
 
				for (dk, dl) in deltas:
					m = k + dk
					n = l + dl
					if (m, n) not in seen:
						stack.append((m, n))
						seen.add((m, n))

			return res

		return max(dfs(i, j) for i in range(M) for j in range(N))
