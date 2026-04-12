# https://leetcode.com/problems/find-the-degree-of-each-vertex/

class Solution(object):
	def findDegrees(self, matrix):
		N = len(matrix)

		numEdges = [0 for _ in range(N)]
		for i in range(N):
			for j in range(N):
				if matrix[i][j] == 1:
					numEdges[i] += 1
					numEdges[j] += 1
					matrix[j][i] = 0
                    
		return numEdges