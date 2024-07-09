# https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/ 

class Solution(object):
	def validStrings(self, n):
		def build(s):
			if len(s) == n:
				return [s]

			res = []
			if s and s[-1] == '0':
				res += build(s + '1')
			else:
				res += build(s + '0')
				res += build(s + '1')

			return res

		return build('')

class Solution(object):
	def validStrings(self, n):
		stack = ['']
		res = []
		while stack:
			s = stack.pop()

			if len(s) == n:
				res.append(s)
				continue

			if s and s[-1] == '0':
				stack.append(s + '1')
			else:
				stack.append(s + '0')
				stack.append(s + '1')

		return res
