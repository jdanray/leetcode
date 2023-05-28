# https://leetcode.com/problems/remove-trailing-zeros-from-a-string/ 

class Solution(object):
	def removeTrailingZeros(self, num):
		i = len(num) - 1
		while num[i] == '0':
			i -= 1

		return num[:i + 1]
