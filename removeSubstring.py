# https://leetcode.com/problems/remove-k-balanced-substrings/

class Solution(object):
	def removeSubstring(self, s, k):
		stack = []
		for c in s:
			if stack and stack[-1][0] == c:
				_, n = stack.pop()
				stack.append((c, n + 1))
			else:
				stack.append((c, 1))

			if len(stack) > 1 and stack[-1] == (')', k) and stack[-2][0] == '(' and stack[-2][1] >= k:
				stack.pop()
				_, n2 = stack.pop()
				if n2 > k:
					stack.append(('(', n2 - k))

		return ''.join(c * n for (c, n) in stack)