# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/

class Solution(object):
	def getNoZeroIntegers(self, n):
		for i in range(1, n):
			if '0' not in str(i) + str(n - i):
				return [i, n - i]

