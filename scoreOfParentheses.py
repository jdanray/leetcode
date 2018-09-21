# https://leetcode.com/problems/score-of-parentheses/description/

class Solution:
	def scoreOfParentheses(self, S):
		def score(S, i, j):
			if i >= j:
				return 0

			k = i
			opened = 1
			while opened > 0:
				k += 1
				if S[k] == '(':
					opened += 1
				else:
					opened -= 1

			if k == i + 1:
				return 1 + score(S, k + 1, j)
			else:
				return 2 * score(S, i + 1, k - 1) + score(S, k + 1, j)

		return score(S, 0, len(S) - 1)
