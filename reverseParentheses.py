# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/ 

class Solution(object):
	def reverseParentheses(self, s):
		N = len(s)
		rev = ""
		right = -1
		for i in range(N - 1, -1, -1):
			if s[i] == '(':
				return self.reverseParentheses(s[:i] + rev + s[right + 1:])
			elif s[i] == ')':
				right = i
				rev = ""
			elif right != -1:
				rev += s[i]
                
		return s
