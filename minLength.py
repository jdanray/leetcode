# https://leetcode.com/problems/minimum-string-length-after-removing-substrings/ 

class Solution(object):
	def minLength(self, s):
		match = {'B': 'A', 'D': 'C'}

		stack = []
		for c in s:
			if c in match and stack and stack[-1] == match[c]:
				stack.pop()
			else:
				stack.append(c)

		return len(stack)
