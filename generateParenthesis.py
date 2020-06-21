# https://leetcode.com/problems/generate-parentheses/

class Solution(object):
	def generateParenthesis(self, n):
		l = n * 2
		def generate(o, c, p):
			if len(p) >= l:
				return [p]

			res = []
			if o < n:
				res += generate(o + 1, c, p + '(')
			if c < o:
				res += generate(o, c + 1, p + ')')

			return res

		return generate(0, 0, '')
