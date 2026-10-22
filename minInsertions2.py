# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/ 

class Solution(object):
	def minInsertions(self, s):
		N = len(s)

		l = 0
		i = 0
		res = 0
		while i < N:
			if s[i] == ')':
				r = 0
				while i < N and s[i] == ')':
					r += 1
					i += 1

				if r % 2 == 1:
					r += 1
					res += 1

				l -= r // 2
				if l < 0:
					res += abs(l)
					l = 0

			if i < N and s[i] == '(':
				l += 1

			i += 1

		res += l * 2

		return res
