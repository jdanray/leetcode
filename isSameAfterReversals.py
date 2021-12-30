# https://leetcode.com/problems/a-number-after-a-double-reversal/ 

class Solution(object):
	def isSameAfterReversals(self, num):
		num = str(num)
		if len(num) == 1:
			return True
		else:
			return num[-1] != '0'
