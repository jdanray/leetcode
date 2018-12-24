# https://leetcode.com/problems/backspace-string-compare/

class Solution:
	def backspaceCompare(self, S, T):
		return self.backspace(S) == self.backspace(T)

	def backspace(self, chars):
		b = []
		for c in chars:
			if c != '#':
				b.append(c)
			elif b:
				b.pop()
		return b
