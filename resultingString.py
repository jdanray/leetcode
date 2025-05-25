# https://leetcode.com/problems/resulting-string-after-adjacent-removals/

class Solution(object):
	def resultingString(self, s):
		N = len(string.ascii_lowercase)
		idx = {c: i for i, c in enumerate(string.ascii_lowercase)}
		adj = lambda a, b: (idx[a] == ((idx[b] + 1) % N)) or (idx[a] == ((idx[b] - 1) % N))

		stack = []
		for c in s:
			if stack and adj(stack[-1], c):
				stack.pop()
			else:
				stack.append(c)

		return ''.join(stack)