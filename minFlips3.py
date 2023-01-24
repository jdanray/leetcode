# https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/ 

class Solution(object):
	def minFlips(self, matrix):
		M = len(matrix)
		N = len(matrix[0])
		deltas = [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]]
	
		mat = 0
		for i in range(M):
			for j in range(N):
				if matrix[i][j] == 1:
					mat |= (1 << (i * N + j))

		queue = collections.deque([[mat, 0]])
		seen = {mat}
		while queue:
			m, f = queue.popleft()

			if m == 0:
				return f

			for i in range(M):
				for j in range(N):
					newm = m
					for di, dj in deltas:
						r = i + di
						c = j + dj
						if 0 <= r < M and 0 <= c < N:
							newm ^= (1 << (r * N + c))

					if newm not in seen:
						seen.add(newm)
						queue.append([newm, f + 1])

		return -1
