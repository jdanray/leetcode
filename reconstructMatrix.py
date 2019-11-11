# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/  

"""
For each 0 <= i < n, there are three possible cases:

Case 0: colsum[i] == 0
Do nothing. We cannot set either res[0][i] or res[1][i] to 1.

Case 1: colsum[i] == 1
We must decide whether to set res[0][i] or res[1][i] to 1. We make the the greedy decision. The row farthest away from hitting its sum gets a 1.

Case 2: colsum[i] == 2
We must set both res[0][i] and res[1][i] to 1
"""

class Solution(object):
	def reconstructMatrix(self, upper, lower, colsum):
		m = 2
		n = len(colsum)
		matrix = [[0 for _ in range(n)] for _ in range(m)]
        
		for i, s in enumerate(colsum):
			if s == 1:
				if upper >= lower:
					matrix[0][i] = 1
					upper -= 1
				else:
					matrix[1][i] = 1
					lower -= 1

			if s == 2:
				matrix[0][i] = 1
				matrix[1][i] = 1
				upper -= 1
				lower -= 1

		return matrix if upper == 0 and lower == 0 else []
