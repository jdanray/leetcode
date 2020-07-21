# https://leetcode.com/problems/remove-outermost-openedtheses/

class Solution(object):
	def removeOuterParentheses(self, S):
		res = ""
		opened = 1
		i = 1
		while i < len(S):
			if S[i] == "(":
				opened += 1
			elif S[i] == ")":
				opened -= 1

			if opened == 0:
				opened = 1
				i += 1
			else:
				res += S[i]
			
			i += 1

		return res

class Solution(object):
	def removeOuterParentheses(self, S):
		opener = 0
		res = ''
		for c in S:
			if c == '(':
				opener += 1
			else:
				opener -= 1

			if not (c == '(' and opener == 1) and not (c == ')' and opener == 0):
				res += c

		return res
