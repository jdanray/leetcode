# https://leetcode.com/problems/simplify-path/

class Solution:
	def simplifyPath(self, path):
		stack = []
		i = 0
		while i < len(path):
			d = ''
			while i < len(path) and path[i] != '/':
				d += path[i]
				i += 1

			if d == '..':
				if stack:
					stack.pop()
			elif d and d != '.':
				stack.append(d)

			i += 1

		return '/' + '/'.join(stack)
