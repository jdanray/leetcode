# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

class Solution(object):
	def generateTheString(self, n):
		if n % 2 == 1:
			return 'p' * n
		else:
			return ('p' * (n - 1)) + 'z' 
