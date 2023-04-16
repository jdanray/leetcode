# https://leetcode.com/problems/row-with-maximum-ones/ 

class Solution(object):
	def rowAndMaximumOnes(self, mat):
		res = [0, 0]
		for i, row in enumerate(mat):
			ones = sum(row)
			if ones > res[1]:
				res = [i, ones]
		return res
