# https://leetcode.com/problems/set-matrix-zeroes/description/

# Time: O(M * N)
# Space: O(M + N)
class Solution(object):
	def setZeroes(self, matrix):
		M = len(matrix)
		N = len(matrix[0])

		row = collections.defaultdict(bool)
		col = collections.defaultdict(bool)
		for i in range(M):
			for j in range(N):
				if matrix[i][j] == 0:
					row[i] = True
					col[j] = True

		for i in range(M):
			for j in range(N):
				if row[i] or col[j]:
					matrix[i][j] = 0

# Time: O(M * N * max(M, N))
# Space: O(1)
class Solution(object):
	def setZeroes(self, matrix):
		M = len(matrix)
		N = len(matrix[0])

		for i in range(M):
			for j in range(N):
				if matrix[i][j] != 0:
					continue

				for k in range(M):
					if matrix[k][j] != 0:
						matrix[k][j] = float('inf')

				for k in range(N):
					if matrix[i][k] != 0:
						matrix[i][k] = float('inf')

		for i in range(M):
			for j in range(N):
				if matrix[i][j] == float('inf'):
					matrix[i][j] = 0

# Time: O(M * N * max(M, N))
# Space: O(M * N)
class Solution(object):
	def setZeroes(self, matrix):
		changed = set()
		for i in range(len(matrix)):
			for j in range(len(matrix[i])):
				if matrix[i][j] == 0 and (i, j) not in changed:
					for k in range(len(matrix[i])):
						if matrix[i][k] != 0:
							matrix[i][k] = 0
							changed.add((i, k))
					for k in range(len(matrix)):
						if matrix[k][j] != 0:
							matrix[k][j] = 0
							changed.add((k, j))

# Time: O(M * N * max(M, N))
# Space: O(1)
class Solution(object):
	def setZeroes(self, matrix):
		INF = 2**32

		M = len(matrix)
		N = len(matrix[0])

		def color(i, j):
			matrix[i][j] = INF
            
			for k in range(M):
				if matrix[k][j] == 0:
					color(k, j)
				else:
					matrix[k][j] = INF

			for k in range(N):
				if matrix[i][k] == 0:
					color(i, k)
				else:
					matrix[i][k] = INF

		for i in range(M):
			for j in range(N):
				if matrix[i][j] == 0:
					color(i, j)

		for i in range(M):
			for j in range(N):
				if matrix[i][j] == INF:
					matrix[i][j] = 0
