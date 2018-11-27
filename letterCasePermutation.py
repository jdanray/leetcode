# https://leetcode.com/problems/letter-case-permutation/description/

class Solution(object):
	def letterCasePermutation(self, S):
		perms = []
		stack = [[0, ""]]
		while stack:
			i, p = stack.pop()
			if i >= len(S):
				perms = [p] + perms
				continue

			stack.append([i + 1, p + S[i]])
			if S[i].isupper():
				stack.append([i + 1, p + S[i].lower()])
			elif S[i].islower():
				stack.append([i + 1, p + S[i].upper()])

		return perms
