# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/ 

class Solution(object):
	def removeOccurrences(self, s, part):
		M = len(s)
		N = len(part)

		for i, c in enumerate(s):
			j = i
			k = 0
			while j < M and k < N and s[j] == part[k]:
				j += 1
				k += 1

			if k >= N:
				return self.removeOccurrences(s[:i] + s[j:], part)

		return s

class Solution(object):
	def removeOccurrences(self, s, part):
		stack = []
		for c in s:
			stack.append(c)

			if len(stack) < len(part):
				continue

			j = len(stack) - 1
			k = len(part) - 1
			while j >= 0 and k >= 0 and stack[j] == part[k]:
				j -= 1
				k -= 1

			if k < 0:
				for _ in range(len(part)):
					stack.pop()

		return ''.join(stack)
