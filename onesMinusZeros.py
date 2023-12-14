# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/ 

class Solution(object):
	def onesMinusZeros(self, grid):
		M = len(grid)
		N = len(grid[0])

		onesRow = [sum(grid[i][j] for j in range(N)) for i in range(M)]
		onesCol = [sum(grid[i][j] for i in range(M)) for j in range(N)]

		return [[2 * onesRow[i] + 2 * onesCol[j] - M - N for j in range(N)] for i in range(M)]

class Solution(object):
	def onesMinusZeros(self, grid):
		M = len(grid)
		N = len(grid[0])

		onesRow = [0 for _ in range(M)]
		onesCol = [0 for _ in range(N)]

		for i in range(M):
			for j in range(N):
				if grid[i][j] == 1:
					onesRow[i] += 1

		for j in range(N):
			for i in range(M):
				if grid[i][j] == 1:
					onesCol[j] += 1

		diff = [[0 for _ in range(N)] for _ in range(M)]
		for i in range(M):
			for j in range(N):
				zerosRow = M - onesRow[i]
				zerosCol = N - onesCol[j]
				diff[i][j] = onesRow[i] + onesCol[j] - zerosRow - zerosCol

		return diff
