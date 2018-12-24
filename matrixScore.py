# https://leetcode.com/problems/score-after-flipping-matrix/description/

class Solution:
	def matrixScore(self, A):
		M, N = len(A), len(A[0])
		# convert each row to its integer equivalent
		matrix = []
		for row in A:
			s = 0
			mul = 1
			for i in range(1, len(row) + 1):
				s += mul * row[-i]
				mul *= 2
			matrix.append(s)

		rowstack = [[matrix, 0]]
		colstack = []
		maxsum = 0
		while rowstack:
			matrix, i = rowstack.pop()
			if i >= len(M):
				maxsum = max(sum(matrix), maxsum)
				continue

			# don't flip row i
			rowstack.append((matrix, i + 1)) 
			colstack.append((matrix, 0))

			# flip row i
			for j in range(N):
				matrix[i] ^= (1 << j)
			rowstack.append((matrix, i + 1))
			colstack.append((matrix, 0))

			while colstack:
				matrix, j = colstack.pop()
				if j >= len(N):
					maxsum = max(sum(matrix), maxsum)
					continue

				# don't flip column j
				colstack.append((matrix, j + 1))
				
				# flip column j
				for i in range(M):
					matrix[i] ^= (1 << j)
				colstack.append((matrix, j + 1))

		return maxsum
