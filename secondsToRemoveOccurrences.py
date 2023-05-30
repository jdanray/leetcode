# https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/ 

class Solution(object):
	def secondsToRemoveOccurrences(self, s):
		N = len(s)

		stack = [list(s)]
		res = 0
		while stack:
			s = stack.pop()

			change = False
			i = 0
			while i < N:
				if i + 1 < N and s[i] + s[i + 1] == '01':
					s[i] = '1'
					s[i + 1] = '0'
					change = True
					i += 2
				else:
					i += 1

			if change:
				stack.append(s)
				res += 1

		return res
