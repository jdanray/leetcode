# https://leetcode.com/problems/pascals-triangle/description/

class Solution:
	def generate(self, n):
		if n <= 0:
			return []
		elif n == 1:
			return [[1]]
		t = [[1], [1, 1]]
		for i in range(1, n - 1):
			t += [[1] + [t[i][j - 1] + t[i][j] for j in range(1, len(t[i]))] + [1]]
		return t
