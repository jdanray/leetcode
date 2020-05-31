# https://leetcode.com/problems/image-smoother/ 

class Solution(object):
	def imageSmoother(self, M):
		m = len(M)
		n = len(M[0])

		for i in range(m):
			for j in range(n):
				M[i][j] = floor(M[i][j])

		R = [[0 for _ in range(n)] for _ in range(m)]
		for i in range(m):
			for j in range(n):
				s = M[i][j]
				c = 1

				if i + 1 < m:
					s += M[i + 1][j]
					c += 1

				if i - 1 >= 0:
					s += M[i - 1][j]
					c += 1

				if j + 1 < n:
					s += M[i][j + 1]
					c += 1

				if j - 1 >= 0:
					s += M[i][j - 1]
					c += 1

				if i + 1 < m and j + 1 < n:
					s += M[i + 1][j + 1]
					c += 1

				if i + 1 < m and j - 1 >= 0:
					s += M[i + 1][j - 1]
					c += 1

				if i - 1 >= 0 and j + 1 < n:
					s += M[i - 1][j + 1]
					c += 1

				if i - 1 >= 0 and j - 1 >= 0:
					s += M[i - 1][j - 1]
					c += 1

				R[i][j] = int(floor(s / c))

		return R
