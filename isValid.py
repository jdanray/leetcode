# https://leetcode.com/problems/valid-parentheses/ 

class Solution(object):
	def isValid(self, s):
		opener = {}
		opener[')'] = '('
		opener['}'] = '{'
		opener[']'] = '['

		stack = []
		for c in s:
			if c in opener.values():
				stack.append(c)
			elif not stack or stack[-1] != opener[c]:
				return False
			else:
				stack.pop()

		return not stack
