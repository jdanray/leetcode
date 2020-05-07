# https://leetcode.com/problems/search-a-2d-matrix-ii/ 

class Solution(object):
	def searchMatrix(self, matrix, target):
		if not matrix:
			return False

		M = len(matrix)
		N = len(matrix[0])

		i = 0
		j = N - 1
		while i < M and j >= 0:
			if matrix[i][j] == target:
				return True
			elif target > matrix[i][j]:
				i += 1
			else:
				j -= 1
		return False


class Solution(object):
	def searchMatrix(self, matrix, target):
		if not matrix:
			return False

		stop = len(matrix[0])
		for row in matrix:
			for j in range(stop):
				entry = row[j]
				if entry == target:
					return True
				if entry > target:
					stop = j
					break
		return False
