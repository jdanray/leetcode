# https://leetcode.com/problems/find-all-groups-of-farmland/ 

class Solution(object):
	def findFarmland(self, land):
		M = len(land)
		N = len(land[0])

		def dfs(i, j):
			if i < 0 or i >= M or j < 0 or j >= N or land[i][j] == 0:
				return [0, 0]

			land[i][j] = 0
            
			a = dfs(i + 1, j)
			b = dfs(i - 1, j)
			c = dfs(i, j + 1)
			d = dfs(i, j - 1)

			res = [i, j]
			if a[0] > res[0] or a[1] > res[1]:
				res = a
			if b[0] > res[0] or b[1] > res[1]:
				res = b
			if c[0] > res[0] or c[1] > res[1]:
				res = c
			if d[0] > res[0] or d[1] > res[1]:
				res = d
                
			return res	

		res = []
		for i in range(M):
			for j in range(N):
				if land[i][j] == 1:
					k, l = dfs(i, j)
					res.append([i, j, k, l])

		return res
