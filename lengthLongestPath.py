# https://leetcode.com/problems/longest-absolute-file-path/submissions/ 

class Solution(object):
	def lengthLongestPath(self, input):
		paths = [['']]
		name = ''
		best = 0
		t = 1
		i = 0
		isfile = False
		while i < len(input):
			if input[i] == '\n' or i == len(input) - 1:
				if i == len(input) - 1:
					name += input[i]

				while t >= len(paths):
					paths.append([])

				fullname = paths[t - 1][-1] + '/' + name
				paths[t].append(fullname)

				if isfile and len(fullname) > best:
					best = len(fullname) - 1

				name = ''
				isfile = False
				t = 1
				i += 1
			elif input[i] != '\t':
				name += input[i]
				if input[i] == '.':
					isfile = True
				i += 1
			else:
				t = 1
				while i < len(input) and input[i] == '\t':
					i += 1
					t += 1

		return best
