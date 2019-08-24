# https://leetcode.com/problems/ambiguous-coordinates/

class Solution(object):
	def decimalize(self, s):
		if len(s) == 1:
			return [s]

		res = []
		if s[0] != '0':
			res.append(s)

		for i in range(1, len(s)):
			n = s[:i]
			d = s[i:]
			if (n[0] != '0' or len(n) == 1) and d[-1] != '0':
				res.append(n + '.' + d)

		return res

	def ambiguousCoordinates(self, S):
		res = []
		for i in range(2, len(S) - 1):
			A = S[1:i]
			B = S[i:-1]
			for a in self.decimalize(A):
				for b in self.decimalize(B):
					res.append("(%s, %s)" % (a, b))
		return res
