# https://leetcode.com/problems/spiral-matrix-iv/ 

class Solution(object):
	def spiralMatrix(self, m, n, head):
		dirs = [0, 1, 0, -1, 0]

		res = [[-1 for _ in range(n)] for _ in range(m)]
		i = 0
		j = 0
		curd = 0
		while head:
			res[i][j] = head.val

			ni = i + dirs[curd]
			nj = j + dirs[curd + 1]
			if ni < 0 or nj < 0 or ni >= m or nj >= n or res[ni][nj] != -1:
				curd = (curd + 1) % 4

			i += dirs[curd]
			j += dirs[curd + 1]

			head = head.next

		return res
