# https://leetcode.com/problems/palindrome-number/description/

class Solution(object):
	def isPalindrome(self, x):
		x = str(x)
		if not x or x[0] == '-':
			return False
		s = 0
		f = len(x) - 1
		for _ in range(len(x) // 2):
			if x[s] != x[f]:
				return False
			s += 1
			f -= 1
		return True
