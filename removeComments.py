# https://leetcode.com/problems/remove-comments/submissions/ 

class Solution(object):
	def removeComments(self, source):
		block = False
		inline = False
		addline = ""
		res = []
		for line in source:
			i = 0
			while i < len(line):
				if not block and not inline and i + 1 < len(line) and line[i] == '/' and line[i + 1] == '*':
					block = True
					i += 2
					continue

				if not block and not inline and i + 1 < len(line) and line[i] == '/' and line[i + 1] == '/':
					inline = True
					i += 2
					continue

				if not inline and not block:
					addline += line[i]

				if block and i + 1 < len(line) and line[i] == '*' and line[i + 1] == '/':
					block = False
					i += 2
					continue

				i += 1

			if not block:
				if addline:
					res.append(addline)
				addline = ""
			inline = False

		return res
