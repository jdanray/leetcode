# https://leetcode.com/problems/maximum-odd-binary-number/ 

class Solution(object):
	def maximumOddBinaryNumber(self, s):
		return ('1' * (s.count('1') - 1)) + ('0' * s.count('0')) + '1'
