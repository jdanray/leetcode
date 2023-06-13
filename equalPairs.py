# https://leetcode.com/problems/equal-row-and-column-pairs/ 

# Time: O(N**3)
# Space: O(1)
class Solution(object):
	def equalPairs(self, grid):
		N = len(grid)

		res = 0
		for i in range(N):
			for j in range(N):
				k = 0
				while k < N and grid[i][k] == grid[k][j]:
					k += 1

				if k == N:
					res += 1

		return res

# Time: O(N**2)
# Space: O(N**2)
class Solution(object):
	def equalPairs(self, grid):
		N = len(grid)

		count = collections.Counter()
		for j in range(N):
			col = tuple(grid[i][j] for i in range(N))
			count[col] += 1

		res = 0
		for i in range(N):
			row = tuple(grid[i][j] for j in range(N))
			res += count[row]

		return res
