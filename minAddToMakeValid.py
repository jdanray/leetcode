# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution(object):
	def minAddToMakeValid(self, s):
		opened = 0
		closed = 0
		for c in s:
			if c == '(':
				opened += 1
			elif opened == 0:
				closed += 1
			else:
				opened -= 1

		return opened + closed

class Solution(object):
	def minAddToMakeValid(self, S):
		opened = 0
		hanging = 0
		for p in S:
			if p == '(':
				opened += 1
			elif p == ')':
				if opened > 0:
					opened -= 1
				else:
					hanging += 1
		return opened + hanging
