# https://leetcode.com/problems/diagonal-traverse/

"""
Precondition(s):

M is an m x n matrix 

Postcondition(s):

O is a list of all elements of the matrix, in diagonal order

Thoughts:

Try a "more-of-the-output" algorithm. That is, try to do the induction on the length of the output, instead of the rows and columns of the input.

Imagine that you have the solution, O, filled in with all the elements in the correct diagonal order. What is the correspondence between any element O[i] and M? In other words: For any i, identify j,k such that O[i] == M[j][k].

Observation: O[0] == M[0][0]

Maybe find a pat routine for each element in the top row, ie, each M[0][k] for all k.

Even though I want to take a functional approach, I might do a state-based analysis where I do the induction on input parameters instead of an output parameter. So, instead of considering each 0 <= i < len(O) and finding the corresponding M[j][k], I'll traverse M in such a way that each M[j][k] that I visit next corresponds to the next element in O.

There seem to be two basic "movements": We sweep down and to the left, and we sweep up-right. 

Update: 

I broke out a pen and paper and drew some pictures. I discovered the way to traverse M by searching for patterns in particular examples that I constructed. That process ultimately resulted in the absurdly thorough (but very clear) program below.
"""

class Solution:
	def findDiagonalOrder(self, matrix):
		if not matrix or not matrix[0]:
			return []

		m = len(matrix)
		n = len(matrix[0])
		i = 0
		j = 0
		rightup = True
		diag = []
		while not (i == m and j == n - 1) and not (i == m - 1 and j == n):
			diag.append(matrix[i][j])
			if rightup:
				if j + 1 >= n:
					i += 1
					rightup = False
				elif i - 1 < 0:
					j += 1
					rightup = False
				else:
					i -= 1
					j += 1
			elif not rightup:
				if i + 1 >= m:
					j += 1
					rightup = True
				elif j - 1 < 0:
					i += 1
					rightup = True
				else:
					i += 1
					j -= 1
		return diag

"""
A perhaps more elegant solution. It's questionable whether it's clearer.
"""

class Solution:
	def shift(self, add, bound, sub, dr):
		if add + 1 >= bound:
			sub += 1
			dr = not dr
		elif sub - 1 < 0:
			add += 1
			dr = not dr
		else:
			add += 1
			sub -= 1

		return (add, sub, dr)

	def findDiagonalOrder(self, matrix):
		if not matrix or not matrix[0]:
			return []

		m = len(matrix)
		n = len(matrix[0])
		i = 0
		j = 0
		rightup = True
		diag = []
		while not (i == m and j == n - 1) and not (i == m - 1 and j == n):
			diag.append(matrix[i][j])

			if rightup:
				(dj, di, dr) = self.shift(j, n, i, rightup)
			else:
				(di, dj, dr) = self.shift(i, m, j, rightup)

			i = di
			j = dj
			rightup = dr

		return diag
