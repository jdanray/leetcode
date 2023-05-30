# https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/ 

class Solution(object):
	def differenceOfDistinctValues(self, grid):
		M = len(grid)
		N = len(grid[0])

		res = [[0 for _ in range(N)] for _ in range(M)]
		for i in range(M):
			for j in range(N):
				left = set()
				k = i - 1
				l = j - 1
				while k >= 0 and l >= 0:
					left.add(grid[k][l])
					k -= 1
					l -= 1

				right = set()
				k = i + 1
				l = j + 1
				while k < M and l < N:
					right.add(grid[k][l])
					k += 1
					l += 1

				res[i][j] = abs(len(left) - len(right))

		return res
