# https://leetcode.com/problems/largest-odd-number-in-string/

class Solution(object):
	def largestOddNumber(self, num):
		for i in range(len(num) - 1, -1, -1):
			if num[i] in '13579':
				return num[:i + 1]
            
		return ''
