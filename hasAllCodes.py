# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/ 

class Solution(object):
	def hasAllCodes(self, s, k):
		codeset = set()
		code = ''
		for i, c in enumerate(s):
			code += c
			if i >= k:
				code = code[1:]

			if i >= k - 1:
				codeset.add(code)

		return len(codeset) == 2 ** k
