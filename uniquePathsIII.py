# https://leetcode.com/problems/unique-paths-iii/

class Solution(object):
	def uniquePathsIII(self, grid):
		M = len(grid)
		N = len(grid[0])
		nempty = 0
		start = (-1, -1)
		end = (-1, -1)
		for i in range(M):
			for j in range(N):
				if grid[i][j] == 1:
					start = (i, j)
				elif grid[i][j] == 2:
					end = (i, j)
				elif grid[i][j] == 0:
					nempty += 1

		res = 0
		stack = [[start, set()]]
		while stack:
			curr, seen = stack.pop()

			if curr == end and len(seen) == nempty + 1:
				res += 1

			for (i, j) in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
				newcurr = (curr[0] + i, curr[1] + j)
				if newcurr[0] < M and newcurr[0] >= 0 and newcurr[1] < N and newcurr[1] >= 0 and newcurr not in seen and grid[newcurr[0]][newcurr[1]] in [0, 2]:
					stack.append([newcurr, seen | {newcurr}])

		return res
