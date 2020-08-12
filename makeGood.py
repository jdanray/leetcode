# https://leetcode.com/problems/make-the-string-great/ 

class Solution(object):
	def makeGood(self, s):
		N = len(string.ascii_lowercase)
		lo2up = {string.ascii_lowercase[i]: string.ascii_uppercase[i] for i in range(N)}
		up2lo = {string.ascii_uppercase[i]: string.ascii_lowercase[i] for i in range(N)}

		stack = []
		for c in s:
			if not stack:
				stack.append(c)
			elif c.isupper() and up2lo[c] == stack[-1]:
				stack.pop()
			elif c.islower() and lo2up[c] == stack[-1]:
				stack.pop()
			else:
				stack.append(c)

		return ''.join(stack)
