# https://leetcode.com/problems/where-will-the-ball-fall/

class Solution(object):
	def findBall(self, grid):
		M = len(grid)
		N = len(grid[0])

		res = []
		for b in range(N):
			j = b
			stuck = False
			for i in range(M):
				jnew = j + grid[i][j]
				if  jnew >= N or jnew < 0 or grid[i][jnew] != grid[i][j]:
					stuck = True
					break
				else:
					j = jnew

			if stuck:
				res.append(-1)
			else:
				res.append(j)

		return res
