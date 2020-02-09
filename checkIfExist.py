# https://leetcode.com/problems/check-if-n-and-its-double-exist/ 

class Solution(object):
	def checkIfExist(self, arr):
		for i, num1 in enumerate(arr):
			for j, num2 in enumerate(arr):
				if i != j and num1 * 2 == num2:
					return True
		return False
