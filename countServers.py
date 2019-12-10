# https://leetcode.com/problems/count-servers-that-communicate/ 

class Solution(object):
    def countServers(self, grid):
		m = len(grid)
		n = len(grid[0])

		rows = collections.defaultdict(int)
		cols = collections.defaultdict(int)
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1:
					rows[i] += 1
					cols[j] += 1

		res = 0
		for i in range(m):
			for j in range(n):
				if grid[i][j] == 1 and (rows[i] > 1 or cols[j] > 1):
					res += 1

		return res
