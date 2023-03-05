# https://leetcode.com/problems/count-total-number-of-colored-cells/

class Solution(object):
	def coloredCells(self, n):
		if n == 1:
			return 1
		else:
			return 4 * (n - 1) + self.coloredCells(n - 1) 
