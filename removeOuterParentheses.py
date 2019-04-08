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
