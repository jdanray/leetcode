# https://leetcode.com/problems/make-the-string-great/ 

class Solution(object):
	def makeGood(self, s):
		stack = []
		for c in s:
			if not stack:
				stack.append(c)
			elif c.isupper() and c.lower() == stack[-1]:
				stack.pop()
			elif c.islower() and c.upper() == stack[-1]:
				stack.pop()
			else:
				stack.append(c)

		return ''.join(stack)
