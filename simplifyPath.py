# https://leetcode.com/problems/simplify-path/

class Solution:
	def simplifyPath(self, path):
		dirs = []
		i = 0
		while i < len(path):
			while i < len(path) and path[i] == '/':
				i += 1

			d = ''
			while i < len(path) and path[i] != '/':
				d += path[i]
				i += 1

			if d == '..':
				if dirs:
					dirs.pop()
			elif d and d != '.':
				dirs.append(d)

		if not dirs: return '/'
		else: return ''.join('/' + d for d in dirs)
