# https://leetcode.com/problems/count-operations-to-obtain-zero/

class Solution(object):
	def countOperations(self, num1, num2):
		res = 0
		while num1 > 0 and num2 > 0:
			if num1 >= num2:
				num1 -= num2
			else:
				num2 -= num1
			res += 1
		return res
