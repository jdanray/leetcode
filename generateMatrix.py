# https://leetcode.com/problems/spiral-matrix-ii/ 

class Solution(object):
	def generateMatrix(self, n):
		dirs = [0, 1, 0, -1, 0]

		res = [[-1 for _ in range(n)] for _ in range(n)]
		i = 0
		j = 0
		curd = 0
		for el in range(n ** 2):
			res[i][j] = el + 1

			ni = i + dirs[curd]
			nj = j + dirs[curd + 1]
			if ni < 0 or nj < 0 or ni >= n or nj >= n or res[ni][nj] != -1:
				curd = (curd + 1) % 4

			i += dirs[curd]
			j += dirs[curd + 1]

		return res
