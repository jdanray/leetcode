# https://leetcode.com/problems/break-a-palindrome/ 

class Solution(object):
	def breakPalindrome(self, palindrome):
		n = len(palindrome) // 2
		i = 0
		while i < n and palindrome[i] == 'a':
			i += 1

		if i < n:
			return palindrome[:i] + 'a' + palindrome[i + 1:]
		elif n > 0:
			return palindrome[:-1] + 'b'
		else:
			return ''
